#!/usr/bin/env python3
# ep15 founder-story photo-dump (kaiandjia 5.8M format): caption-driven, no VO,
# slide+fade caption animation, pop-ins, SFX layer (ding/pop/whoosh). Music added in-app.
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = "/Users/yash/Library/Mobile Documents/com~apple~CloudDocs/Documents/Yash/The Bon Pet/creative"
B   = "%s/ep15_founderstory_build" % ROOT
S   = "%s/src" % B
A   = "%s/assets" % B; os.makedirs(A, exist_ok=True)
SEG = "%s/seg" % B; os.makedirs(SEG, exist_ok=True)
SFX = "%s/sfx" % ROOT
FRF = "%s/fonts/FredokaOne.ttf" % ROOT
FF  = "/opt/homebrew/bin/ffmpeg"
W,H = 1080,1920
CREAM=(245,235,220); TEAL=(22,67,61); ORANGE=(217,108,73)

def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR", c[-1]); print(r.stderr[-800:]); raise SystemExit(1)
def font(sz): return ImageFont.truetype(FRF, sz)

# (dur, src, inpoint_or_None, caption_lines, sfx)
BEATS=[
 (2.6,"IMG_0083.MOV",0.5,  ["We've taken $0 out of","our own pet food brand."],"boom"),
 (2.0,"IMG_2999.JPG",None, ["On purpose. Here's the story:"],None),
 (2.2,"IMG_2998.MOV",2.0,  ["2024: Nic and I were two","software engineers with furkids."],None),
 (2.2,"Nice_beef_ingredients_photo.jpg",None,["Then we read what's actually","in kibble. So we started cooking."],None),
 (2.0,"broken_table.png",None,["It was NOT glamorous."],"pop"),
 (2.2,"fair22_IMG_8548.JPG",None,["Launch day: zero customers."],None),
 (2.2,"fair21_IMG_8541.JPG",None,["Nobody would risk their furkid","on an unknown brand. Fair enough."],None),
 (2.4,"fair10_IMG_7887.JPG",None,["So we made a bet: one pack","FREE. For anyone. No questions."],"ding"),
 (1.6,"fair11_IMG_7896.JPG",None,["We lose $9 on every free pack."],"chaching"),
 (1.6,"fair12_IMG_7902.JPG",None,["Thousands of our own","dollars. Gone."],"pop"),
 (1.6,"fair17_IMG_7953.JPG",None,["But look at these faces."],"pop"),
 (1.6,"fair16_IMG_7935.JPG",None,["(we'd do it again)"],"pop"),
 (2.2,"fair03_IMG_6787.JPG",None,["Hundreds of pet parents later..."],"riser_lead"),
 (2.2,"fair14_IMG_7913.JPG",None,["4.8 stars. AAFCO certified.","Formulas 100% public."],"sparkle"),
 (2.2,"fair00_IMG_6766.JPG",None,["And the free pack? Still live","today. Even the kangaroo."],None),
 (2.4,"IMG_3004.JPG",None, ["We're not here to get rich.","We're here to feed furkids."],"bell"),
 (3.0,"IMG_2997.MOV",0.2,  ["Follow along. We're just","getting started 🐾"],None),
]
VID_END=round(sum(b[0] for b in BEATS),2)

def fit_image(src,out):
    im=Image.open(src).convert("RGB")
    ar=im.width/im.height
    if ar > W/H:
        nh=H; nw=int(ar*H)
        im=im.resize((nw,nh),Image.LANCZOS).crop(((nw-W)//2,0,(nw-W)//2+W,H))
    else:
        nw=W; nh=int(W/ar)
        im=im.resize((nw,nh),Image.LANCZOS).crop((0,max(0,(nh-H)//3),W,max(0,(nh-H)//3)+H))
    im.save(out)

paths=[]; t=0; starts=[]
for i,(dur,src,inp,lines,sfx) in enumerate(BEATS):
    starts.append(round(t,2)); t+=dur
    out="%s/s%02d.mp4"%(SEG,i); paths.append(out); d=round(dur,3)
    fsrc="%s/%s"%(S,src)
    if src.lower().endswith((".mov",".mp4")):
        vf="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p"
        run([FF,"-y","-ss",str(inp or 0),"-t",str(d),"-i",fsrc,"-vf",vf,"-r","30","-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-an",out])
    else:
        tmp="%s/_p%02d.png"%(A,i); fit_image(fsrc,tmp)
        vf="scale=1080:1920,setsar=1,fps=30,format=yuv420p"
        run([FF,"-y","-loop","1","-t",str(d),"-i",tmp,"-vf",vf,"-r","30","-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-an",out])
print("beats:",starts,"end",VID_END)

with open("%s/list.txt"%SEG,"w") as f:
    for p in paths: f.write("file '%s'\n"%p)
run([FF,"-y","-f","concat","-safe","0","-i","%s/list.txt"%SEG,"-r","30","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-an","%s/base.mp4"%B])

# ---- caption PNGs (kaiandjia style: white, 2 lines, center, shadow) ----
def story_caption(lines, sz=62):
    f=font(sz)
    tmp=Image.new("RGBA",(4,4)); d=ImageDraw.Draw(tmp)
    ws=[int(d.textlength(l,font=f)) for l in lines]
    asc,desc=f.getmetrics(); lh=asc+desc+8
    w=max(ws)+48; h=lh*len(lines)+28
    im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    for li,l in enumerate(lines):
        x=(w-ws[li])//2; y=14+li*lh
        for ox,oy in ((3,4),(2,4),(4,3),(0,2)):
            d.text((x+ox,y+oy),l,font=f,fill=(0,0,0,170))
        d.text((x,y),l,font=f,fill=(255,255,255))
    return im

overlays=[]  # (path, x_expr, y_expr, t0, t1)
for i,(dur,src,inp,lines,sfx) in enumerate(BEATS):
    t0=starts[i]; t1=round(t0+dur,2)
    im=story_caption(lines)
    if im.width>1000: im=im.resize((1000,int(im.height*1000/im.width)),Image.LANCZOS)
    p="%s/cap%02d.png"%(A,i); im.save(p)
    yt=1180
    # slide-up + settle: y animates from yt+50 to yt over 0.22s
    yexpr="if(lt(t\\,%s)\\,%d+50*(1-(t-%s)/0.22)\\,%d)"%(round(t0+0.22,2),yt,t0,yt)
    overlays.append((p,"(W-w)/2",yexpr,t0,t1))

# logo badge
logo=Image.open("%s/Logo/circle_icon_only.png"%ROOT).convert("RGBA")
disc=Image.new("RGBA",(logo.width,logo.height),(0,0,0,0)); dd=ImageDraw.Draw(disc)
dd.ellipse([0,0,logo.width-1,logo.height-1],fill=CREAM+(235,)); disc.alpha_composite(logo)
disc.resize((120,120)).save("%s/logo.png"%A)
overlays.append(("%s/logo.png"%A,"48","70",0.0,VID_END))

inputs=["-i","%s/base.mp4"%B]
for o in overlays: inputs+=["-i",o[0]]
fc=""; last="[0:v]"
for i,o in enumerate(overlays):
    fc+="%s[%d:v]overlay=x=%s:y=%s:enable='between(t,%s,%s)'[v%d];"%(last,i+1,o[1],o[2],o[3],o[4],i)
    last="[v%d]"%i

# ---- SFX audio bed ----
sfx_events=[]
for i,(dur,src,inp,lines,sfx) in enumerate(BEATS):
    if sfx=="riser_lead":
        sfx_events.append((max(0,starts[i]-1.45),"riser"))
    elif sfx:
        sfx_events.append((starts[i]+0.08,sfx))
    elif not BEATS[i][1].lower().endswith((".mov",".mp4")) and i>0:
        sfx_events.append((starts[i]+0.02,"shutter"))
a_inputs=[]; a_fc=""
for j,(at,kind) in enumerate(sfx_events):
    a_inputs+=["-i","%s/%s.wav"%(SFX,kind)]
    a_fc+="[%d:a]adelay=%d|%d,volume=%s,apad=whole_dur=%s[a%d];"%(len(overlays)+1+j,int(at*1000),int(at*1000),{"ding":"0.7","bell":"0.7","boom":"0.85","riser":"0.6","shutter":"0.45","sparkle":"0.7","chaching":"0.7","pop":"0.55","whoosh":"0.55"}.get(kind,"0.55"),VID_END,j)
amix="".join("[a%d]"%j for j in range(len(sfx_events)))
a_fc+="%samix=inputs=%d:duration=first:dropout_transition=0:normalize=0,alimiter=limit=0.85[aout]"%(amix,len(sfx_events))
fc=fc+a_fc

run([FF,"-y",*inputs,*a_inputs,"-filter_complex",fc,"-map",last,"-map","[aout]",
     "-t",str(VID_END),"-c:v","libx264","-crf","19","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","%s/ep15_founderstory_v3.mp4"%B])
print("DONE %s/ep15_founderstory_v3.mp4 end=%s sfx=%d"%(B,VID_END,len(sfx_events)))
