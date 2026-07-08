#!/usr/bin/env python3
# Word-level transcription of EXISTING footage, so cuts can be picked from raw takes (formats A/B),
# not just from a script. Thariq (@trq212) transcribe.py analog: word-level Whisper + incremental
# cache (only new/changed clips do work) + a transcript-fixes layer (Whisper silently drops/mangles words).
# Usage: python transcribe_footage.py take1.mov take2.mov -o build/tx --lang en
import os, sys, json, subprocess, hashlib, argparse

FF = os.environ.get("REEL_FFMPEG", "/opt/homebrew/bin/ffmpeg")

def wav16k(src, wav):
    subprocess.run([FF,"-y","-i",src,"-ac","1","-ar","16000",wav], capture_output=True)

def transcribe(src, out_dir, lang, fixes):
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(src))[0]
    sig = hashlib.sha1((os.path.abspath(src)+str(os.path.getmtime(src))+lang).encode()).hexdigest()[:10]
    out_json = os.path.join(out_dir, f"{base}.{sig}.words.json")
    if os.path.exists(out_json):                       # incremental: skip clips already transcribed
        return out_json, True
    wav = os.path.join(out_dir, f".{base}.wav"); wav16k(src, wav)
    raw_dir = os.path.join(out_dir, ".raw"); os.makedirs(raw_dir, exist_ok=True)
    # mlx-whisper large-v3-turbo, word timestamps, FORCED language (auto-detect mishears accented English)
    subprocess.run(["mlx_whisper", wav, "--model","mlx-community/whisper-large-v3-turbo",
                    "--language",lang, "--word-timestamps","True",
                    "--output-format","json","--output-dir",raw_dir], capture_output=True)
    raw = os.path.join(raw_dir, os.path.splitext(os.path.basename(wav))[0]+".json")
    words = []
    for seg in json.load(open(raw)).get("segments", []):
        for w in seg.get("words", []):
            tok = w["word"].strip()
            words.append({"t": round(w["start"],2), "end": round(w["end"],2),
                          "word": tok, "display": fixes.get(tok, tok)})
    json.dump({"src": src, "words": words}, open(out_json,"w"), ensure_ascii=False)
    for f in (wav, raw):
        try: os.remove(f)
        except OSError: pass
    return out_json, False

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("clips", nargs="+")
    ap.add_argument("-o","--out", default="build/tx")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--fixes", default="transcript-fixes.json")
    a = ap.parse_args()
    fixes = json.load(open(a.fixes)) if os.path.exists(a.fixes) else {}
    for c in a.clips:
        p, cached = transcribe(c, a.out, a.lang, fixes)
        print(("cached " if cached else "wrote  ") + p)
