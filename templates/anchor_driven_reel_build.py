#!/usr/bin/env python3
# ep14 FINAL - anchor-driven build: all timings derive from vo_words.json, safe to regen VO.
import os, subprocess, json
from PIL import Image, ImageDraw, ImageFont

ROOT = "/Users/yash/Library/Mobile Documents/com~apple~CloudDocs/Documents/Yash/The Bon Pet/creative"
B   = "%s/fur-the-record/ep14_sousvide_build" % ROOT
BR  = "%s/fur-the-record/broll/cook" % ROOT
ET  = "%s/fur-the-record/broll/video" % ROOT
LP  = os.path.expanduser("~/Library/CloudStorage/SynologyDrive-sync/04_talent/Lola/Feeding Lola POV")
A   = "%s/assets" % B; os.makedirs(A, exist_ok=True)
SEG = "%s/seg" % B; os.makedirs(SEG, exist_ok=True)
FRF = "%s/fonts/FredokaOne.ttf" % ROOT
EMO = "/System/Library/Fonts/Apple Color Emoji.ttc"
FF  = "/opt/homebrew/bin/ffmpeg"
TEAL=(22,67,61); ORANGE=(217,108,73); CREAM=(245,235,220)
W,H = 1080,1920

def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode != 0:
        print("ERR", c[-1]); print(r.stderr[-700:]); raise SystemExit(1)
def font(sz): return ImageFont.truetype(FRF, sz)

# ---- VO word timing → beat anchors ----
words = json.load(open("%s/vo_words.json" % B))  # [(t, word), ...]
DISPLAY = {"soo":"sous", "Soo":"Sous", "veed":"vide", "veed.":"vide.", "veed,":"vide,", "veed?":"vide?"}
def anchor(seq_word, occurrence=1):
    n=0
    for t,w in words:
        if w.strip(".,?!").lower()==seq_word.lower():
            n+=1
            if n==occurrence: return t
    raise SystemExit("anchor not found: %s#%d"%(seq_word,occurrence))
def anchor_phrase(w1,w2,w3=None):
    for i,(t,w) in enumerate(words):
        if w.strip(".,?!").lower()==w1.strip(".,?!").lower() and i+1<len(words) and words[i+1][1].strip(".,?!").lower()==w2.strip(".,?!").lower():
            if w3 is None or (i+2<len(words) and words[i+2][1].strip(".,?!").lower()==w3.lower()):
                return t
    raise SystemExit("phrase anchor not found: %s %s"%(w1,w2))

b_twice   = anchor_phrase("That","is","nearly")
b_heat    = anchor_phrase("At","that")
b_spray   = anchor_phrase("So","they")
b_we      = anchor_phrase("We","cook")
b_hot     = anchor_phrase("Hot","enough")
b_gentle  = anchor_phrase("Gentle","enough")
b_realmv  = anchor_phrase("Real","meat")
b_weighed = anchor("weighed",1)
b_sealed  = anchor("sealed",1)
b_lookswhy= anchor_phrase("That","is","why")
b_fur     = anchor_phrase("And","fur-the-record?")
b_follow  = anchor_phrase("Follow","for")
vo_end    = words[-1][0] + 0.7
VID_END   = round(vo_end + 2.3, 1)

b_bag_split  = round(b_we + (b_hot-b_we)*0.5, 2)
b_food_split = round(b_lookswhy + (b_fur-b_lookswhy)*0.5, 2)
p1 = round(b_fur + (b_follow-b_fur)*0.43, 2)
p2 = round(b_fur + (b_follow-b_fur)*0.78, 2)

# ---- segments ----
segs=[
 (b_twice-0.0,        "vid","%s/IMG_4500.MOV"%ET, 0.0),
 (b_heat-b_twice,     "vid","%s/IMG_4167.MOV"%BR, 0.8),
 (b_spray-b_heat,     "vid","%s/IMG_4494.MOV"%ET, 1.5),
 (b_we-b_spray,       "still","%s/patent_receipt.png"%B, 0),
 (b_bag_split-b_we,   "vid","%s/Flow_VID_20250216_120558_02_003.MOV"%BR, 6.0),
 (b_hot-b_bag_split,  "vid","%s/IMG_4165.MOV"%BR, 52.0),
 (b_gentle-b_hot,     "vid","%s/IMG_6975.MOV"%BR, 0.2),
 (b_realmv-b_gentle,  "vid","%s/IMG_1994.MOV"%BR, 0.3),
 (b_weighed-b_realmv, "vid","%s/IMG_2017.MOV"%BR, 2.0),
 (b_sealed-b_weighed, "vid","%s/IMG_7028.MOV"%BR, 0.4),
 (b_lookswhy-b_sealed,"vid","%s/IMG_4161.MOV"%BR, 2.0),
 (b_food_split-b_lookswhy,"vid","%s/IMG_7027.MOV"%BR, 7.0),
 (b_fur-b_food_split, "vid","%s/IMG_2752.MOV"%LP, 1.0),
 (p1-b_fur,           "vid","%s/28bba380-973c-47e4-9fb8-13af7381b126.mp4"%ET, 5.0),
 (p2-p1,              "vid","%s/IMG_2744.MOV"%LP, 3.0),
 (b_follow-p2,        "vid","%s/IMG_2756.MOV"%LP, 0.3),
 (VID_END-b_follow,   "vid","%s/IMG_2755.MOV"%LP, 1.0),
]
paths=[]; t=0; starts=[]
for i,(dur,kind,src,inp) in enumerate(segs):
    starts.append(round(t,2)); t+=dur
    out="%s/s%02d.mp4"%(SEG,i); paths.append(out); d=round(dur,3)
    if kind=="vid":
        vf="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p"
        run([FF,"-y","-ss",str(inp),"-t",str(d),"-i",src,"-vf",vf,"-r","30","-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-an",out])
    else:
        im=Image.open(src).convert("RGBA")
        canvas=Image.new("RGB",(W,H),CREAM)
        sc=min(W*0.98/im.width, H*0.66/im.height)
        nw,nh=int(im.width*sc),int(im.height*sc)
        canvas.paste(im.resize((nw,nh),Image.LANCZOS),((W-nw)//2,(H-nh)//2))
        tmp="%s/_still%02d.png"%(A,i); canvas.save(tmp)
        vf="scale=1080:1920,setsar=1,fps=30,format=yuv420p"
        run([FF,"-y","-loop","1","-t",str(d),"-i",tmp,"-vf",vf,"-r","30","-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-an",out])
print("segment starts:", starts, "total", round(t,2))

with open("%s/list.txt"%SEG,"w") as f:
    for p in paths: f.write("file '%s'\n"%p)
run([FF,"-y","-f","concat","-safe","0","-i","%s/list.txt"%SEG,"-r","30","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-an","%s/base.mp4"%B])

# ---- overlays ----
def sticker(text, accent=None, box=TEAL, txt=CREAM, acol=ORANGE, sz=64, rot=-2):
    f=font(sz); pad=(46,24); rad=38
    tmp=Image.new("RGBA",(4,4)); d=ImageDraw.Draw(tmp)
    tw=d.textlength(text,font=f); asc,desc=f.getmetrics(); th=asc+desc
    w=int(tw+pad[0]*2); h=int(th+pad[1]*2)
    im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,w-1,h-1],radius=rad,fill=box)
    x=pad[0]
    for wd in text.split(" "):
        col=acol if (accent and wd.strip(",.?!:").upper()==accent.upper()) else txt
        d.text((x,pad[1]-2),wd+" ",font=f,fill=col); x+=d.textlength(wd+" ",font=f)
    if rot: im=im.rotate(rot,expand=True,resample=Image.BICUBIC)
    return im

def emoji(ch,size=140):
    im=Image.new("RGBA",(200,200),(0,0,0,0)); d=ImageDraw.Draw(im)
    ef=None
    for px in (160,96,64):
        try: ef=ImageFont.truetype(EMO,px); break
        except OSError: continue
    d.text((0,0),ch,font=ef,embedded_color=True)
    bbox=im.getbbox()
    if bbox: im=im.crop(bbox)
    return im.resize((size,size))

caps=[]
def save(name,img): img.save("%s/%s.png"%(A,name)); return "%s/%s.png"%(A,name)
def cap(text,accent,t0,t1,y=380,box=TEAL,acol=ORANGE,sz=64,pop=True):
    p=save("c%d"%len(caps),sticker(text,accent,box=box,acol=acol,sz=sz))
    caps.append([p,"(W-w)/2",y,round(t0,2),round(t1,2),pop])
def emo(ch,x,y,t0,t1):
    p=save("e%d"%(100+len(caps)),emoji(ch)); caps.append([p,str(x),y,round(t0,2),round(t1,2),True])

cap("kibble: cooked at 150°C","150°C",0.2,b_twice-0.1,box=ORANGE,acol=CREAM)
cap("ours: just 80°C","80°C",b_twice+0.2,b_heat-0.1)
cap("that heat KILLS the good stuff","KILLS",b_heat+0.2,b_spray-0.2,box=ORANGE,acol=CREAM)
cap("so vitamins get sprayed on AFTER","AFTER",b_spray+0.2,b_we-0.2,y=330)
cap("yes, there's a patent for it",None,b_spray+0.2,b_we-0.2,y=1560,box=ORANGE,acol=CREAM,sz=52)
cap("we cook sous vide at 80°C","80°C",b_we+0.2,b_hot-0.2)
cap("kills the bad stuff","bad",b_hot+0.2,b_gentle-0.2,box=ORANGE,acol=CREAM)
cap("keeps the nutrients","nutrients",b_gentle+0.2,b_realmv-0.1)
cap("real meat + veg",None,b_realmv+0.2,b_weighed-0.1,box=ORANGE,acol=CREAM)
cap("weighed to the GRAM","GRAM",b_weighed+0.2,b_sealed-0.1)
cap("sealed + cooked slow",None,b_sealed+0.2,b_lookswhy-0.2,box=ORANGE,acol=CREAM)
cap("so it still looks like FOOD","FOOD",b_lookswhy+0.2,b_fur-0.2)
cap("gently cooked, exactly that 🤝",None,b_fur+0.3,b_follow-0.2,box=ORANGE,acol=CREAM)
cap("follow for more food truths","follow",b_follow+0.2,VID_END-0.1)

emo("🔥",830,540,0.2,b_twice-0.1)
emo("♨️",830,540,b_we+0.2,b_hot-0.2)
emo("🥦",830,540,b_gentle+0.2,b_realmv-0.1)
emo("⚖️",830,540,b_weighed+0.2,b_sealed-0.1)
emo("🐾",830,1560,b_follow+0.2,VID_END-0.1)

# ---- read-along captions (word-synced), white + shadow, pop-in ----
def phrase_groups(ws, maxw=4):
    groups=[]; cur=[]
    for t,w in ws:
        cur.append((t,w))
        if len(cur)>=maxw or w.rstrip().endswith(('.',',','?','!')):
            groups.append(cur); cur=[]
    if cur: groups.append(cur)
    return groups
def readalong_png(text, sz=58):
    f=font(sz)
    tmp=Image.new("RGBA",(4,4)); d=ImageDraw.Draw(tmp)
    tw=int(d.textlength(text,font=f)); asc,desc=f.getmetrics(); th=asc+desc
    im=Image.new("RGBA",(tw+46,th+34),(0,0,0,0)); d=ImageDraw.Draw(im)
    for ox,oy in ((3,4),(2,4),(4,3)):
        d.text((23+ox,12+oy),text,font=f,fill=(0,0,0,150))
    d.text((23,12),text,font=f,fill=(255,255,255))
    return im
groups=phrase_groups(words)
for gi,g in enumerate(groups):
    t0=g[0][0]
    t1=groups[gi+1][0][0] if gi+1<len(groups) else vo_end
    disp=" ".join(DISPLAY.get(w,w) for _,w in g).strip()
    im=readalong_png(disp)
    if im.width>980: im=im.resize((980,int(im.height*980/im.width)),Image.LANCZOS)
    caps.append([save("ra%d"%gi,im),"(W-w)/2",1250,round(t0,3),round(t1,3),True])

logo=Image.open("%s/Logo/circle_icon_only.png"%ROOT).convert("RGBA")
disc=Image.new("RGBA",(logo.width,logo.height),(0,0,0,0)); dd=ImageDraw.Draw(disc)
dd.ellipse([0,0,logo.width-1,logo.height-1],fill=CREAM+(235,)); disc.alpha_composite(logo)
disc.resize((120,120)).save("%s/logo.png"%A)
caps.append(["%s/logo.png"%A,"48",70,0.0,VID_END,False])

# pop-in: 1.13x for first 0.09s
final=[]
for (pth,x,y,t0,t1,pop) in caps:
    if pop and t1-t0>0.2:
        im=Image.open(pth)
        big=im.resize((int(im.width*1.13),int(im.height*1.13)),Image.LANCZOS)
        pb=pth.replace(".png","_b.png"); big.save(pb)
        tp=round(t0+0.09,3)
        final.append((pb,x,y,t0,tp)); final.append((pth,x,y,tp,t1))
    else:
        final.append((pth,x,y,t0,t1))

inputs=["-i","%s/base.mp4"%B,"-i","%s/vo.mp3"%B]
for c in final: inputs+=["-i",c[0]]
fc=""; last="[0:v]"
for i,c in enumerate(final):
    fc+="%s[%d:v]overlay=x=%s:y=%s:enable='between(t,%s,%s)'[v%d];"%(last,i+2,c[1],c[2],c[3],c[4],i)
    last="[v%d]"%i
fc=fc.rstrip(";")
run([FF,"-y",*inputs,"-filter_complex",fc,"-map",last,"-map","1:a","-af","apad=pad_dur=3",
     "-t",str(VID_END),"-c:v","libx264","-crf","19","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","%s/ep14_sousvide_FINAL.mp4"%B])
print("DONE %s/ep14_sousvide_FINAL.mp4  VID_END=%s  overlays=%d"%(B,VID_END,len(final)))
