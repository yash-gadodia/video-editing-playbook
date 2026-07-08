#!/usr/bin/env python3
# Reusable reel machinery adopted from Thariq (@trq212) code-driven editing:
# composable JSON artifacts, incremental segment cache ("new work only"), low-res proxy first.
# Import into a build script instead of re-hardcoding cut/scale/concat every time.
import os, json, hashlib, subprocess

FF = os.environ.get("REEL_FFMPEG", "/opt/homebrew/bin/ffmpeg")
PROXY = os.environ.get("REEL_PROXY") == "1"          # REEL_PROXY=1 -> fast low-res preview
AUDIO = os.environ.get("REEL_AUDIO") == "1"          # REEL_AUDIO=1 -> keep natural/diegetic sound (ASMR).
# Music is NEVER baked in (copyright); it is added in-app. Natural footage sound IS safe to bake.
# A still, or a video spec with {"mute": true}, gets a silent 48k stereo track so concat stays uniform.

# Iterate at proxy res/fps; ship full-res. Rendering time is THE bottleneck (Thariq), so make it optional.
W, H   = (540, 960) if PROXY else (1080, 1920)
FPS    = 15 if PROXY else 30
CRF    = "28" if PROXY else "20"
PRESET = "ultrafast" if PROXY else "veryfast"

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print("ERR", cmd[-1]); print(r.stderr[-800:]); raise SystemExit(1)
    return r

SILENCE = "anullsrc=channel_layout=stereo:sample_rate=48000"

def _sig(spec):
    # cache key = everything that changes this segment (spec + render profile, incl. audio mode)
    payload = json.dumps(spec, sort_keys=True) + f"|{W}x{H}@{FPS}c{CRF}|a{int(AUDIO)}"
    return hashlib.sha1(payload.encode()).hexdigest()[:12]

def cut_segment(spec, cache_dir):
    # spec = {"src","in","dur","mute"?} for footage, or {"still","dur","bg"?} for a letterboxed still.
    # Incremental cache: identical spec+profile reuses the encoded file, skips ffmpeg entirely.
    os.makedirs(cache_dir, exist_ok=True)
    out = os.path.join(cache_dir, f"seg_{_sig(spec)}.mp4")
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return out, True
    d = round(float(spec["dur"]), 3)
    still = "still" in spec
    silent = still or spec.get("mute")            # stills + muted clips get a silent track under AUDIO
    cmd = [FF, "-y"]
    if still:
        cmd += ["-loop","1","-t",str(d),"-i",spec["still"]]
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
              f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x{spec.get('bg','FFF3DF')},setsar=1,fps={FPS},format=yuv420p")
    else:
        cmd += ["-ss",str(spec.get("in",0)),"-t",str(d),"-i",spec["src"]]
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS},format=yuv420p"
    if AUDIO and silent:
        cmd += ["-f","lavfi","-t",str(d),"-i",SILENCE]
    cmd += ["-vf",vf,"-r",str(FPS),"-c:v","libx264","-crf",CRF,"-preset",PRESET,"-pix_fmt","yuv420p"]
    if not AUDIO:
        cmd += ["-an"]
    elif silent:
        cmd += ["-map","0:v","-map","1:a","-c:a","aac","-ar","48000","-ac","2","-shortest"]
    else:
        cmd += ["-af","aresample=48000","-ac","2","-c:a","aac"]   # keep the clip's natural sound
    cmd += [out]
    run(cmd)
    return out, False

def build_segments(cutlist_path, cache_dir):
    # Read the editable cutlist JSON, render each segment (cached), return ordered paths + start offsets.
    segs = json.load(open(cutlist_path))["segments"]
    paths, starts, t, hits = [], [], 0.0, 0
    for s in segs:
        p, cached = cut_segment(s, cache_dir)
        paths.append(p); starts.append(round(t, 2)); t += round(float(s["dur"]), 3); hits += cached
    print(f"segments: {len(segs)} ({hits} cached, {len(segs)-hits} rendered) total={round(t,2)}s "
          f"{'PROXY' if PROXY else 'FULL'} {W}x{H}@{FPS}")
    return paths, starts, round(t, 2)

def concat(paths, out_path):
    # concat-FILTER re-encode (never -c copy: timestamp discontinuities freeze the fps filter)
    lst = out_path + ".list.txt"
    with open(lst, "w") as f:
        for p in paths: f.write("file '%s'\n" % p)
    a = ["-c:a","aac","-ar","48000","-ac","2"] if AUDIO else ["-an"]
    run([FF,"-y","-f","concat","-safe","0","-i",lst,"-r",str(FPS),
         "-c:v","libx264","-crf",CRF,"-preset",PRESET,"-pix_fmt","yuv420p",*a,out_path])
    return out_path

def load_fixes(path="transcript-fixes.json"):
    # display corrections for words Whisper/TTS mangle (e.g. {"soo":"sous","Nick":"Nic"})
    return json.load(open(path)) if os.path.exists(path) else {}
