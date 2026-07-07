#!/usr/bin/env python3
import json, subprocess, base64, urllib.request, os

B = os.path.dirname(os.path.abspath(__file__))
VID = "TN2BXBkR7YG4jqAxrym3"
KEY = subprocess.run(["security","find-generic-password","-s","elevenlabs-bonpet","-w"],capture_output=True,text=True).stdout.strip()

SCRIPT = open(os.path.join(B,"vo_script.txt")).read().strip()

req = urllib.request.Request(
    f"https://api.elevenlabs.io/v1/text-to-speech/{VID}/with-timestamps",
    data=json.dumps({
        "text": SCRIPT,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability":0.14,"style":0.68,"similarity_boost":0.78,"speed":1.10},
    }).encode(),
    headers={"xi-api-key":KEY,"Content-Type":"application/json"})
resp = json.loads(urllib.request.urlopen(req, timeout=180).read())
open(os.path.join(B,"vo_raw.mp3"),"wb").write(base64.b64decode(resp["audio_base64"]))
json.dump(resp["alignment"], open(os.path.join(B,"vo_align.json"),"w"))
subprocess.run(["/opt/homebrew/bin/ffmpeg","-y","-i",os.path.join(B,"vo_raw.mp3"),
    "-af","highpass=f=75,loudnorm=I=-16:TP=-1.5",os.path.join(B,"vo.mp3")],capture_output=True)

al = resp["alignment"]; chars=al["characters"]; st=al["character_start_times_seconds"]
words=[]; cur=""; t0=None
for c,t in zip(chars,st):
    if c.strip()=="" :
        if cur: words.append((round(t0,2),cur)); cur=""
    else:
        if not cur: t0=t
        cur+=c
if cur: words.append((round(t0,2),cur))
json.dump(words, open(os.path.join(B,"vo_words.json"),"w"), ensure_ascii=False)
dur = subprocess.run(["/opt/homebrew/bin/ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",os.path.join(B,"vo.mp3")],capture_output=True,text=True).stdout.strip()
print("VO done:", dur, "s;", len(words), "words")
for t,w in words: print(t, w)
