#!/usr/bin/env python3
# ep15 VO version: same photo-dump, beats anchor-driven from vo_words.json, VO + SFX mixed.
import os, subprocess, json
from PIL import Image, ImageDraw, ImageFont

ROOT = "/Users/yash/Library/Mobile Documents/com~apple~CloudDocs/Documents/Yash/The Bon Pet/creative"
B   = "%s/ep15_founderstory_build" % ROOT
S   = "%s/src" % B
A   = "%s/assets" % B; os.makedirs(A, exist_ok=True)
SEG = "%s/segvo" % B; os.makedirs(SEG, exist_ok=True)
SFX = "%s/sfx" % ROOT
FRF = "%s/fonts/FredokaOne.ttf" % ROOT
FF  = "/opt/homebrew/bin/ffmpeg"
W,H = 1080,1920
CREAM=(245,235,220)

def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR", c[-1]); print(r.stderr[-800:]); raise SystemExit(1)
def font(sz): return ImageFont.truetype(FRF, sz)

words = json.load(open("%s/vo_words.json" % B))
def anchor_phrase(*ws):
    ws=[w.strip(".,?!…").lower() for w in ws]
    for i,(t,w) in enumerate(words):
        if w.strip(".,?!…").lower()==ws[0]:
            ok=True
            for k,q in enumerate(ws[1:],1):
                if i+k>=len(words) or words[i+k][1].strip(".,?!…").lower()!=q: ok=False; break
            if ok: return t
    raise SystemExit("anchor not found: %s"%(ws,))

# (src, inpoint, caption_lines, sfx, anchor_words)
BEATS=[
 ("IMG_0083.MOV",0.5,  ["We've taken $0 out of","our own pet food brand."],"boom",("We've","taken")),
 ("IMG_2999.JPG",None, ["On purpose. Here's the story:"],None,("On","purpose")),
 ("IMG_2998.MOV",2.0,  ["2024: Nic and I were two","software engineers with furkids."],None,("2024",)),
 ("Nice_beef_ingredients_photo.jpg",None,["Then we read what's actually","in kibble. So we started cooking."],None,("Then","we")),
 ("broken_table.png",None,["It was NOT glamorous."],"pop",("It","was")),
 ("fair22_IMG_8548.JPG",None,["Launch day: zero customers."],None,("Launch",)),
 ("fair21_IMG_8541.JPG",None,["Nobody would risk their furkid","on an unknown brand. Fair enough."],None,("Nobody",)),
 ("fair10_IMG_7887.JPG",None,["So we made a bet: one pack","FREE. For anyone. No questions."],"ding",("So","we","made")),
 ("fair11_IMG_7896.JPG",None,["We lose $9 on every free pack."],"chaching",("We","lose")),
 ("fair12_IMG_7902.JPG",None,["Thousands of our own","dollars. Gone."],"pop",("Thousands",)),
 ("fair17_IMG_7953.JPG",None,["But look at these faces."],"pop",("But","look")),
 ("fair16_IMG_7935.JPG",None,["(we'd do it again)"],"pop",("We'd","do")),
 ("fair03_IMG_6787.JPG",None,["Hundreds of pet parents later..."],"riser_lead",("Hundreds",)),
 ("fair14_IMG_7913.JPG",None,["4.8 stars. AAFCO certified."],"sparkle",("4.8",)),
 ("site_whatspublic.jpg",None,["Formulas 100% public."],None,("Formulas",)),
 ("fair00_IMG_6766.JPG",None,["And the free pack? Still live","today. Even the kangaroo."],None,("And","the","free")),
 ("IMG_3004.JPG",None, ["We're not here to get rich.","We're here to feed furkids."],"bell",("We're","not")),
 ("IMG_2997.MOV",0.2,  ["Follow along. We're just","getting started 🐾"],None,("Follow","along")),
]
starts=[anchor_phrase(*b[4]) for b in BEATS]
vo_end=words[-1][0]+0.8
VID_END=round(vo_end+1.6,1)
durs=[round((starts[i+1] if i+1<len(BEATS) else VID_END)-starts[i],3) for i in range(len(BEATS))]
print("starts:",[round(s,2) for s in starts]); print("durs:",durs)

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

paths=[]
for i,(src,inp,lines,sfx,anc) in enumerate(BEATS):
    out="%s/s%02d.mp4"%(SEG,i); paths.append(out); d=durs[i]
    fsrc="%s/%s"%(S,src)
    if src.lower().endswith((".mov",".mp4")):
        vf="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p"
        run([FF,"-y","-ss",str(inp or 0),"-t",str(d),"-i",fsrc,"-vf",vf,"-r","30","-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-an",out])
    else:
        tmp="%s/_pv%02d.png"%(A,i); fit_image(fsrc,tmp)
        vf="scale=1080:1920,setsar=1,fps=30,format=yuv420p"
        run([FF,"-y","-loop","1","-t",str(d),"-i",tmp,"-vf",vf,"-r","30","-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-an",out])

with open("%s/list.txt"%SEG,"w") as f:
    for p in paths: f.write("file '%s'\n"%p)
run([FF,"-y","-f","concat","-safe","0","-i","%s/list.txt"%SEG,"-r","30","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-an","%s/base_vo.mp4"%B])

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

overlays=[]
for i,(src,inp,lines,sfx,anc) in enumerate(BEATS):
    t0=starts[i]; t1=round(t0+durs[i],2)
    im=story_caption(lines)
    if im.width>1000: im=im.resize((1000,int(im.height*1000/im.width)),Image.LANCZOS)
    p="%s/capv%02d.png"%(A,i); im.save(p)
    yt=1180
    yexpr="if(lt(t\\,%s)\\,%d+50*(1-(t-%s)/0.22)\\,%d)"%(round(t0+0.22,2),yt,round(t0,3),yt)
    overlays.append((p,"(W-w)/2",yexpr,round(t0,3),t1))

logo=Image.open("%s/Logo/circle_icon_only.png"%ROOT).convert("RGBA")
disc=Image.new("RGBA",(logo.width,logo.height),(0,0,0,0)); dd=ImageDraw.Draw(disc)
dd.ellipse([0,0,logo.width-1,logo.height-1],fill=CREAM+(235,)); disc.alpha_composite(logo)
disc.resize((120,120)).save("%s/logo.png"%A)
overlays.append(("%s/logo.png"%A,"48","70",0.0,VID_END))

inputs=["-i","%s/base_vo.mp4"%B]
for o in overlays: inputs+=["-i",o[0]]
fc=""; last="[0:v]"
for i,o in enumerate(overlays):
    fc+="%s[%d:v]overlay=x=%s:y=%s:enable='between(t,%s,%s)'[v%d];"%(last,i+1,o[1],o[2],o[3],o[4],i)
    last="[v%d]"%i

sfx_events=[]
for i,(src,inp,lines,sfx,anc) in enumerate(BEATS):
    if sfx=="riser_lead": sfx_events.append((max(0,starts[i]-1.45),"riser"))
    elif sfx: sfx_events.append((starts[i]+0.05,sfx))
    elif not src.lower().endswith((".mov",".mp4")) and i>0: sfx_events.append((starts[i]+0.02,"shutter"))

VOL={"ding":"0.45","bell":"0.45","boom":"0.6","riser":"0.4","shutter":"0.3","sparkle":"0.45","chaching":"0.45","pop":"0.35"}
a_inputs=["-i","%s/vo.mp3"%B]; a_fc="[%d:a]apad=whole_dur=%s[avo];"%(len(overlays)+1,VID_END)
for j,(at,kind) in enumerate(sfx_events):
    a_inputs+=["-i","%s/%s.wav"%(SFX,kind)]
    a_fc+="[%d:a]adelay=%d|%d,volume=%s,apad=whole_dur=%s[a%d];"%(len(overlays)+2+j,int(at*1000),int(at*1000),VOL.get(kind,"0.4"),VID_END,j)
amix="[avo]"+"".join("[a%d]"%j for j in range(len(sfx_events)))
a_fc+="%samix=inputs=%d:duration=first:dropout_transition=0:normalize=0,alimiter=limit=0.9[aout]"%(amix,1+len(sfx_events))
fc=fc+a_fc

run([FF,"-y",*inputs,*a_inputs,"-filter_complex",fc,"-map",last,"-map","[aout]",
     "-t",str(VID_END),"-c:v","libx264","-crf","19","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","%s/ep15_founderstory_VO.mp4"%B])
print("DONE %s/ep15_founderstory_VO.mp4 end=%s sfx=%d"%(B,VID_END,len(sfx_events)))
