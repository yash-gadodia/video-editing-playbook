#!/usr/bin/env python3
"""Framing helpers. Two rules, enforced in code so nobody has to remember them:

1. Never compute a crop from ffprobe's width/height in Python. Phone clips carry a rotation
   side-data tag; ffprobe reports the STORED raster (3840x2160) while ffmpeg decodes the
   DISPLAYED one (2160x3840). A Python crop built on the stored size slices a narrow strip out
   of the wrong axis. `crop_to()` builds the crop from iw/ih inside ffmpeg, so it is always
   measured on the decoded frame.
2. Never trust a segment you have not looked at. `shot_sheet()` renders first / middle / last
   frame of every cut segment into one PNG. Open it before compositing. Every shipped
   framing failure so far would have been visible in this sheet.

    from framing import decoded_size, crop_to, shot_sheet
    vf = f"{crop_to(9, 16, cx=0.5, cy=0.4)},scale=1080:1920:flags=lanczos,fps=30,setsar=1"
    shot_sheet(segs, "build/shots.png")

CLI: `python3 framing.py size CLIP...` prints the decoded size and whether the stored raster
was rotated. `python3 framing.py sheet OUT.png SEG...` renders the contact sheet.
"""
import json, os, subprocess, sys


def _probe(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height:stream_side_data=rotation:stream_tags=rotate", "-of", "json", path],
        capture_output=True, text=True, check=True)
    return json.loads(r.stdout)["streams"][0]


def decoded_size(path):
    """(width, height) of the frame ffmpeg will actually hand to filters, rotation applied."""
    s = _probe(path)
    w, h = s["width"], s["height"]
    rot = 0
    for sd in s.get("side_data_list", []):
        if "rotation" in sd:
            rot = int(sd["rotation"])
    rot = rot or int(s.get("tags", {}).get("rotate", 0) or 0)
    if abs(rot) % 180 == 90:
        w, h = h, w
    return w, h, rot


def crop_to(aw, ah, cx=0.5, cy=0.5):
    """ffmpeg crop expression for target aspect aw:ah, evaluated on the decoded frame.

    cx/cy are the fraction of the spare width/height to discard on the left/top, so 0.5 is a
    centre crop, 0.0 pins the crop to the left/top edge. If the source is already the target
    aspect the crop is the identity, so a portrait clip going to 9:16 is scale-only."""
    cw = f"min(iw\\,ih*{aw}/{ah})"
    ch = f"min(ih\\,iw*{ah}/{aw})"
    return (f"crop='floor({cw}/2)*2':'floor({ch}/2)*2'"
            f":'(iw-{cw})*{cx}':'(ih-{ch})*{cy}'")


def shot_sheet(segments, out_png, thumb_h=320):
    """One row per segment: first, middle and last frame. Look at it before compositing."""
    tiles = []
    for i, seg in enumerate(segments):
        n = int(subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
             "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", seg],
            capture_output=True, text=True, check=True).stdout.strip().rstrip(","))
        picks = sorted({0, max(n // 2, 0), max(n - 1, 0)})
        sel = "+".join(f"eq(n\\,{p})" for p in picks)
        tile = f"{out_png}.seg{i}.png"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", seg, "-vf",
             f"select='{sel}',scale=-2:{thumb_h},tile={len(picks)}x1", "-frames:v", "1", tile],
            check=True)
        tiles.append(tile)
    inputs = sum((["-i", t] for t in tiles), [])
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex",
                    "".join(f"[{i}:v]" for i in range(len(tiles))) + f"vstack=inputs={len(tiles)}",
                    out_png], check=True)
    for t in tiles:
        os.remove(t)
    print(f"shot sheet -> {out_png}  ({len(segments)} segments, open it before compositing)")
    return out_png


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "size":
        for p in sys.argv[2:]:
            w, h, rot = decoded_size(p)
            print(f"{p}: decoded {w}x{h}" + (f" (stored raster rotated {rot})" if rot else ""))
    elif len(sys.argv) > 3 and sys.argv[1] == "sheet":
        shot_sheet(sys.argv[3:], sys.argv[2])
    else:
        print(__doc__)
