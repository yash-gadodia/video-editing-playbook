#!/usr/bin/env python3
"""Durable word-level transcript cache.

Transcribing 4K source repeatedly is the single most expensive avoidable step in a
build. This keeps one copy per source file, keyed by a content fingerprint, in a
cache that lives next to the footage library so every job and every machine hits it.

    python3 transcript_cache.py get  <video ...>     # transcribe (or reuse) -> prints cache paths
    python3 transcript_cache.py text <video>         # print the plain transcript
    python3 transcript_cache.py grep <pattern>       # search every cached transcript
    python3 transcript_cache.py ls                   # list what's cached

Cache root defaults to $TRANSCRIPT_CACHE, else the Synology footage root.
Entries are keyed by sha1(basename + size + mtime), so re-encoding or moving a file
re-transcribes it, but a plain re-run never does.
"""
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CACHE_ROOT = Path(
    os.environ.get(
        "TRANSCRIPT_CACHE",
        "/Users/yash/Library/CloudStorage/SynologyDrive-sync/_transcripts",
    )
)
MODEL = os.environ.get("WHISPER_MODEL", "mlx-community/whisper-large-v3-turbo")
INDEX = CACHE_ROOT / "index.csv"


def fingerprint(path: Path) -> str:
    st = path.stat()
    raw = f"{path.name}|{st.st_size}|{int(st.st_mtime)}"
    return hashlib.sha1(raw.encode()).hexdigest()[:16]


def read_index() -> dict:
    if not INDEX.exists():
        return {}
    with INDEX.open() as fh:
        return {row["key"]: row for row in csv.DictReader(fh)}


def write_index(rows: dict) -> None:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    with INDEX.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["key", "source", "duration", "words"])
        w.writeheader()
        for row in sorted(rows.values(), key=lambda r: r["source"]):
            w.writerow(row)


def transcribe(path: Path, force: bool = False) -> Path:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    key = fingerprint(path)
    out_json = CACHE_ROOT / f"{key}.json"
    if out_json.exists() and not force:
        return out_json

    wav = CACHE_ROOT / f"{key}.wav"
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(path),
         "-ac", "1", "-ar", "16000", "-vn", str(wav)],
        check=True,
    )
    subprocess.run(
        ["mlx_whisper", str(wav), "--model", MODEL, "--output-dir", str(CACHE_ROOT),
         "--output-name", key, "--word-timestamps", "True", "--output-format", "json"],
        check=True, stdout=subprocess.DEVNULL,
    )
    wav.unlink(missing_ok=True)

    data = json.loads(out_json.read_text())
    (CACHE_ROOT / f"{key}.txt").write_text(data.get("text", "").strip() + "\n")

    segs = data.get("segments") or []
    idx = read_index()
    idx[key] = {
        "key": key,
        "source": str(path),
        "duration": f"{segs[-1]['end']:.1f}" if segs else "0",
        "words": str(sum(len(s.get("text", "").split()) for s in segs)),
    }
    write_index(idx)
    return out_json


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    cmd = sys.argv[1]

    if cmd == "get":
        for arg in sys.argv[2:]:
            p = Path(arg).resolve()
            existed = (CACHE_ROOT / f"{fingerprint(p)}.json").exists()
            out = transcribe(p)
            print(f"{'CACHED ' if existed else 'NEW    '} {p.name} -> {out}")
        return 0

    if cmd == "text":
        p = Path(sys.argv[2]).resolve()
        transcribe(p)
        print((CACHE_ROOT / f"{fingerprint(p)}.txt").read_text())
        return 0

    if cmd == "grep":
        pat = re.compile(sys.argv[2], re.I)
        for row in read_index().values():
            js = CACHE_ROOT / f"{row['key']}.json"
            if not js.exists():
                continue
            for seg in json.loads(js.read_text()).get("segments", []):
                if pat.search(seg.get("text", "")):
                    print(f"{Path(row['source']).name}  "
                          f"{seg['start']:7.2f}-{seg['end']:7.2f}  {seg['text'].strip()}")
        return 0

    if cmd == "ls":
        for row in read_index().values():
            print(f"{row['key']}  {row['duration']:>8}s  {row['words']:>6}w  {row['source']}")
        return 0

    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
