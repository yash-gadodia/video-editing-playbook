# The Video Editing Playbook

A framework for editing + publishing short-form videos **mostly autonomously with an AI coding agent** (we use Claude Code). This is the distilled version of 30+ videos of trial-and-error. Read it top to bottom once, then keep it open as a checklist.

The north star: **a postable-quality video out of ONE prompt.** Every iteration trains toward that. Treat every correction as a permanent rule, not a one-off.

> **Quality-upgrade roadmap in flight: see §10.** The pipeline is migrating from ffmpeg+PIL to Remotion-first, and the QA gate is being upgraded into a "screening room" that verifies motion + audio, not just still frames. Until a phase is marked DONE in §10, the recipes below remain the working method.

---

## 0. The mental model (why this works the way it does)

1. **The agent has no ears and judges from still frames, not motion.** So lip-sync, audio clicks, jitter, and "is that a hard cut or natural movement" are INVISIBLE to it. The whole pipeline is designed to avoid needing those judgments. When something depends on them, the rule is "say *please verify by playback*", never claim it's fixed.
2. **Every story is premise → conflict → resolution.** Lead with the conflict/hook in the first ~3s (carry it past 5s+). One concept per video. Short and punchy (30-45s for most; longer only when depth demands it and retention data supports it).
3. **We don't sell in reels.** Even "why we're different / better" stays educational. End on "follow along / see for yourself", never a trial pitch. Selling kills shareability and breaks the founder-as-educator moat. (Testimonial videos are the one exception - they can end on a trial CTA.)
4. **The bar is shareability, not polish.** "Would your friend with a cat forward this?" If no, rework the concept, not the styling. Real footage + brand text + CTA = a competent *ad*, and people don't share ads.
5. **First-party retention data beats every blog.** After a reel posts, get the IG Insights retention graph and cut the next one based on where viewers actually dropped. Most "best practices" listicles are folklore - only watch-time, completion, replays, and shares are verified ranking signals.

---

## 1. The four formats

### A. Founder series (talking-head → captioned documentary cut)
Story-driven. Founder grit/loss/stakes beats explainers. 30-60s talk + ~3.8s end card. Soft "Follow" ending (sells the story, not the product).

### B. Testimonial reel (customer interviews)
Same recipe as founder series, but: speaker changes are free jump cuts (no masking), eating-B-roll cutaways between speakers, and the end card CAN be a trial CTA (testimonials sell product).

### C. UGC / eating / product reel (the "fun" reel)
Curated library clips + Gen-Z brand-sticker captions + emoji + beat-synced cuts + logo badge. Match-cut variant (lock a constant object to one screen spot so it "stays" while pets swap). One concept, conflict-first hook.

### D. BTS / tech / "how we built X" (scripted-VO + screenshots) - **the most automatable**
The go-to for explainer/product/tech content. Write a tight ~28-30s VO script on ONE topic, the VO is generated (or recorded), the founder sends 5-6 screenshots mapped to script beats, the agent edits full-frame cards + word-timed captions. No old footage to fight, no lip-sync to verify → fully automatable end to end. **This is the format to lean on for autopilot.**

---

## 2. The end-to-end pipeline (the recipe)

### Step 1 - Script (formats A/D) or curate (formats B/C)
- **Format D (preferred for autopilot):** write a ~28-30s VO script, ONE topic, problem-first, brand voice. Tell the founder exactly which 5-6 screenshots/clips to send (a shotlist).
- **Format A/B:** transcribe the raw takes, pick the story arc from the transcript.
- **Format C:** grep the footage-library index, build a contact sheet of midframes, pick the strong shots.

### Step 2 - VO
Three options, in order of automation:
1. **ElevenLabs cloned voice** (best for autopilot) - clone the founder's voice, generate VO per script via API. Inherently clean (no clicks/room noise/lip-sync). See §5.
2. **Founder records one clean continuous take** in a quiet room (NOT stitched from jump-cut talking-head audio - stitching breaks natural flow and reads jittery).
3. **Camera audio** - last resort. Always prefer the **mic-pair** track over the camera's room audio (see §6).

### Step 3 - Transcribe (for caption timing)
`mlx-whisper`, model `whisper-large-v3-turbo`, `--word-timestamps True`, **force the language flag** (auto-detect hears accented English as another language). Extract 16k mono wav first. Use the small model to scout all takes, large-turbo for the chosen clip's caption-grade words.

### Step 4 - Build overlays (PIL → transparent PNGs)
Our ffmpeg build has **no libass, no drawtext, no freetype**. So *every* caption/label/card/emoji is a transparent PNG drawn in Pillow, composited with the `overlay` filter. Build:
- **Hook card** - eyebrow + 2-line headline (display font, brand fill + stroke).
- **Word-timed captions** - 3-4 word chunks, semibold, brand fill + stroke, keyword words in the accent color. Clamp each caption `end = min(end, next.start - 0.02)` so two never overlap (overlap = garbled double-text).
- **B-roll cutaways** - real photos cover-cropped to 1080x1920; screenshots as rounded cards on a brand bg + label. **Pixelate PII** (downscale 14x then back up).
- **Emoji pops** - Apple Color Emoji via PIL (size MUST be 160 + `embedded_color=True`, then resize ~200px, rotate ±6-10°). ~8-10 per 60s, each tied to a spoken beat, clear of faces + captions.
- **Logo badge** - the brand mark on a filled disc (reads on any bg), in a corner.
- **End card** - logo wordmark + "Follow our journey" + handle, xfade in over the last 0.45s.

### Step 5 - Render (ffmpeg filter graph)
- **Layer order: cutaways first, captions ON TOP, watermark last.** (Captions under photos = wasted render.)
- Looped-PNG overlays: `-loop 1 -t (end+1)` spanning output-time 0..end, with absolute-time `fade=st=...`. (Getting this wrong = overlay invisible after ~2s.)
- LIVE-card MP4s: shift to output time with `setpts=PTS-STARTPTS+start/TB`.
- **NEVER `-c copy` concat** for an overlay base - timestamp discontinuities freeze the fps filter. Always concat-FILTER re-encode. ffprobe every trimmed seg (library trims come out short) and rebuild overlay times from ACTUAL cumulative durations.
- `xfade`/`acrossfade` need `settb=AVTB` on both inputs and the SAME duration on audio + video (or they desync over the chain).
- Output: 1080x1920, H.264, ~crf 18-19, `-preset veryfast` (IG re-compresses anyway).
- **Audio chain MUST end with `aresample=48000` + output `-ar 48000 -ac 2`.** `loudnorm` upsamples to 96kHz → macOS preview plays it SILENT. This bug has bitten multiple times.
- Add a ~25ms `afade` in+out on each audio segment boundary (jump-cut concat clicks otherwise).

### Step 6 - QA GATE (mandatory, before saying "done")
Run an automated `qa_check.py` (reusable, copied per job). It deterministically catches what eyeballing misses:
- **Coverage** - every output moment must be covered by a b-roll OR be an intended face beat. Any uncovered span >0.04s outside `face_beats` = BLOCKER (a 0.1-0.3s "camera-base peek" is jarring and unacceptable). B-roll `end` MUST equal the next shot's `start` exactly. **Cover through the very END** before the endcard.
- **Freezes** - any cutaway shorter than its manifest window holds its last frame = blocker. Fix by re-trimming the adjacent clip longer (verify the source has the length).
- **Soft/dark clips** - sharpness (edge-variance) + brightness score; flag low ones.
- **Silent intro** - the hook visual must play OVER the VO, never a silent cold-open clip prepended.

Exit non-zero = do NOT ship. Then read rendered frames densely at every transition + face beat. **Only then** open for review.

### Step 7 - Handoff + publish
- Reveal the final mp4 + draft the caption in brand voice → copy it to the clipboard (no em-dashes, no literal promo code in the body). No hashtags unless asked.
- The founder adds trending audio at low volume in the IG composer (master ships SILENT - baked-in commercial audio = copyright strike + reach loss). Music is never baked in.
- A few days after posting: get the IG Insights retention graph, cut the next video off it.

---

## 3. The hard rules (these caused the most pain)

| Rule | Why |
|---|---|
| **NO em-dashes (—) or en-dashes (–). Ever.** Grep before shipping. | Instant AI-tell. Use hyphens, commas, parentheses, or restructure. |
| **Never repeat the same footage** within a video; minimise across videos. | Reads as "the f***, repeated the same shot". Build a footage-variety board before rendering. |
| **Default to NO face intercuts** - keep the talking head UNDER b-roll (lips not visible). | Mic-audio offset never has to be lip-sync-precise. Only show visible lips if video+audio are the SAME file AND the take is static. |
| **Don't sell in reels.** End on follow/see-for-yourself. | Selling breaks the educator moat + kills shares. |
| **Cutaways must be SHARP, well-lit, and have MOTION** (hands working, ingredients, transformation). No static equipment shots. | A machine sitting there = dead air. Pick for energy first, then topical fit. |
| **Whisper UNDERESTIMATES word-end times** - extend each segment past the word-end into the following pause. | Trimming exactly at the transcript word-end chops the acoustic tail = "cut halfway through his word". |
| **Open on the most intriguing PROCESS shot, problem-first, close on a pets-eating montage** (2-3 different pets). | The visual hook + social-proof bookend. |
| **Be decisive.** When the directive is clear, use best judgment and execute. Don't ping-pong options or ask "which clip?" mid-task. | The whole point is one-prompt output. |
| **Verify before claiming.** Read the rendered frames at changed timestamps before saying it's fixed. | No exceptions. |
| **Never conclude "footage doesn't exist" from a filename search.** | Library files are named content-blind (`IMG_4155.MOV`). Find by FOLDER + visual sample. |
| **Things the agent CAN'T self-verify** (no ears, frames-only): audio clicks, lip-sync, motion jitter, hard-cut-vs-natural-movement. | Design so you don't need them; else say "please verify by ear". |

When clipping a short cut out of a finished video that used xfade transitions: **start the extract AFTER the incoming crossfade completes and end BEFORE the outgoing one begins** - else the first/last ~0.12s is a ghost-blend of two shots ("weird jittery thing").

---

## 4. The brand design system (ours - swap in your own tokens)

**Fonts:**
- Display / headlines: **Fredoka One**
- Captions / body: **Fredoka SemiBold** (use the static TTF - the variable one defaults to Light)

**Colors:**
- Primary teal `#16433D` · cream `#FFF3DF` / `#FFFCFA` · tan `#EDDDC0`
- Orange `#D96C49` (keyword pops + promo CTAs ONLY, never beside a green primary)
- Accent pink `#E12B65` / soft pink `#F5C2D1` (eyebrows, labels)

**Caption recipe:** word-timed 3-4 word chunks, semibold ~68px, cream fill + teal stroke ~5px, y≈1400, auto-shrink to ≤980px wide. Keyword words (numbers, time stamps, disaster words) in orange.

**Buttons / pills:** radius 12px (not full pill), primary solid teal + white text, orange for promo.

Whatever your tokens are: encode them ONCE as constants in the overlay scripts, so every video is automatically on-brand and recognizable as a series.

---

## 5. Tooling / environment

**Our machine (macOS, Apple Silicon):**
- ffmpeg (Homebrew): **no libass, no drawtext, no freetype** → all text via PIL PNGs.
- Beat detection + audio cross-correlation in **pure Python** (stdlib `wave`+`array`) when numpy isn't around - but see §10 Phase 1: a proper venv with numpy/scipy/librosa is the planned upgrade.
- `mlx-whisper` for transcription (venv).
- PIL/Pillow for all overlays.

**ElevenLabs** (AI VO so the founder isn't limited by their own reading):
- Store the API key securely (keychain/env var); the header is `xi-api-key`, NOT Bearer.
- Voice cloning needs the **Starter plan (~US$5/mo)** - free tier blocks instant cloning.
- **Clone the founder's own voice, not a stock voice** (stock sounds American; a clone keeps local founder authenticity).
- TTS: `POST /v1/text-to-speech/<voice_id>` with `model_id: eleven_multilingual_v2` → mp3, drop into the render pipeline as the VO track. Use the `with-timestamps` variant to get word timings for captions.
- The clone's energy ceiling is the TRAINING DATA, not the settings. Energetic settings that helped: stability ~0.14, style ~0.66, speed 1.08. For real excitement, record a hyped training take.

**Heavy renders** → offload to an always-on machine in tmux (laptop preps the self-contained job folder where the render step is pure ffmpeg + PNGs; rsync it over; launch detached in tmux; poll for a `DONE`/`FAIL` sentinel). Survives the laptop sleeping. The render machine won't have your footage library synced - **ship the source clips**, don't expect library paths to resolve.

---

## 6. Footage sourcing

- Keep the whole footage library (ours: a Synology NAS, ~100GB) **indexed in a CSV** - grep the index to locate assets, don't browse. Parse with a real CSV parser, not `awk -F,` (paths contain commas). Don't bulk-download; hydrate cloud placeholders on access.
- Curate WITHOUT watching everything: extract one midpoint frame per candidate clip (ffmpeg `-ss mid -frames:v 1`), tile into a **contact sheet** (`-vf tile=6xN`), read the sheet, pick the strong shots.
- Organize by folder: cook/kitchen process b-roll, pets eating, customer UGC, finished output. Check the process-footage folder FIRST for "how it's made" content.
- The "money shot" may live in someone's phone Photos library, not the shared drive. Ask.

**Library limits (learned the hard way):**
- A pets-eating folder can look big (23 clips) yet contain only ~4 distinct animals - sequential filenames usually mean one session, one pet. A montage-heavy reel exhausts distinct subjects fast; track subjects, not clip counts, and keep asking for fresh footage of NEW animals.
- Customer UGC (reposted stories) has baked-in usernames + text overlays = unusable as clean b-roll. UGC works for social-proof cuts only.
- Keep a per-video **clip usage ledger** (which source clip went into which published video). It is what makes the "never repeat footage" rule enforceable by query instead of memory.

**Two-phone founder takes:** shoot every founder take on two phones - one camera angle (room audio, DON'T use the audio) and one with the wireless lav mic (clean audio, ALWAYS use). **Video can come from either angle; audio ALWAYS from the mic phone.** Sync the two via envelope cross-correlation (extract 16k mono WAVs, correlate a clear-speech window).

---

## 7. Reusable machinery (patterns, not one-offs)

- **Cutplan-as-JSON:** per-episode build scripts carry the cutplan as data (`CUTS`/`ZOOMS`/`CARDS`/word-FIXES) so a new episode = edit the data, not the code.
- **One full-recipe UGC-reel script** (match-cut align + beat-sync + per-cut brand sticker captions + emoji + logo + intro/CTA + music): clone it and edit the segment list.
- **A founder-series job folder** including `qa_check.py` (the QA gate) - copy per job.
- **BTS/screen-walkthrough machinery** (format D): asset builder + live-card renderer + final render script. Two card types: LIVE cards (pre-rendered MP4s for clean screens) and STILL cards (PIL PNGs with PII baked-in-blurred).

**Match-cut recipe** (locked-frame: "the frame doesn't move, only the subject changes"): pick clips sharing one setup (same dish, floor, angle); measure the anchor object's center + width per clip from a normalized frame with a 10% grid overlay; per clip compute the zoom `k` so the crop stays in bounds (`k=max(TDW/dw, TX/cx, (1-TX)/(1-cx), TY/cy, (1-TY)/(1-cy))*1.03`), then scale + crop to pin the anchor to the same target spot. Handheld footage drifts within a clip too - add `deshake` before the align (the zoom-crop hides its edge fills). Drop clips whose anchor is far off-center (recentering forces too much zoom).

**Beat-synced cuts with zero audio libs:** extract mono 22050 wav → frame energy (hop 512) → onset = positive energy flux → autocorrelation over plausible BPM for tempo → beat phase = offset maximizing summed onset. Set each segment duration to a whole number of beats, and trim the music to START at the first-beat offset so downbeats align with t=0. Beat-sync is track-specific: change the song → re-detect + re-build.

---

## 8. The autopilot target (what "automatic" looks like)

The most automatable path, end to end, with the founder only providing a topic + a few screenshots:

```
topic  →  agent writes ~28-30s VO script (brand voice, problem-first, one concept)
       →  ElevenLabs cloned voice generates the VO mp3
       →  founder sends 5-6 screenshots mapped to the shotlist the agent gave
       →  agent: whisper-times the VO, builds caption + card + emoji + logo PNGs,
          pixelates PII, renders the ffmpeg graph
       →  qa_check.py = 0 blockers  →  read frames to confirm
       →  reveal file + copy caption  →  founder adds trending audio + posts
       →  (a few days later) retention graph → next video
```

The stated goal: a video up in ~10 minutes from a transcript.

---

## 9. The self-learning loop

This framework is monotonic: **each video should need fewer corrections than the last.** Before starting any video, read this doc. After each session, append every new directive/correction as a permanent rule here. If a note gets repeated, that's a miss - a rule wasn't applied; tighten it.

---

## 10. Quality-upgrade roadmap

**Diagnosis (first principles):** the rules above are strong; the tooling hit a ceiling. Every recurring human-caught correction (jitter, audio clicks, chopped words, flat VO, repeated footage, pacing) lives in the exact blind spots the pipeline can't see - the agent judges from still frames and has no ears. And the ffmpeg+PIL stack spends most of its complexity fighting its own limitations (no drawtext → PNG overlays, xfade timebase bugs, the aresample silent-audio bug, zoompan jitter). Fix the root causes, not more checklist items.

### Phase 1 - Give the agent eyes and ears (screening-room QA)
The single biggest unlock: convert the "invisible to the agent" defect class into deterministic pre-ship checks.
- **Frame-burst motion checks:** at every cut point, extract a dense 8-10 frame strip (~15fps) + compute inter-frame pixel diffs → programmatically detects jitter, ghost xfade blends, freezes, drift. Read the strip (not a single still) to judge motion.
- **Real audio toolchain:** a venv with numpy/scipy/librosa. Unlocks: click detection at cut boundaries (sample discontinuity), loudness curves, dead-air detection, VO energy score (pitch + energy variance → flag flat reads before a human hears them).
- **Chopped-word check:** re-transcribe the RENDERED output with whisper, diff against the script. A word that didn't survive the render was chopped at a cut. Deterministic, no ears needed.
- **Fold everything into one `qa_check.py` "screening room" gate** with per-format profiles: coverage + freeze + jitter + click + chopped-word + loudness + safe-zone + sharpness + variety. Exit non-zero = never reaches the human.

### Phase 2 - Consolidate on Remotion as THE engine (IN PROGRESS - first full reel shipped natively 2026-07-02)
Remotion (React-coded video) does natively + deterministically everything the PIL pipeline hand-rolls, kills the zoompan-jitter class, and adds polish (springs, draw-on circles, stat count-ups, kinetic type).
- **Component library:** `<WordCaptions>` (whisper JSON in, clamped no-overlap, keyword pops), `<Sticker>`, `<DrawCircle>`, `<StatCountUp>`, `<CompositionBar>`, `<EatingMontage>`, `<HookTitle>`, `<EndCard>`, `<LogoBadge>` - with safe zones + brand tokens as enforced constants, not conventions.
- **Data-driven `<Reel>`:** one composition that takes a cutplan JSON (segments, broll windows, captions, emoji, VO path). A new video = write JSON + pick clips, zero new code. This is the real path to one-prompt.
- ffmpeg's role shrinks to clip pre-normalization. Iterate on 540x960/15fps proxy renders; full-res only to ship. Scrub cuts live in `npm run studio`.
- ⚠️ Check the Remotion license: the free tier is for companies of ≤3 people; bigger teams need a Company License before shipping regularly.

### Phase 3 - Scored, tagged shot library
One-time pass over the footage index → `shots.json`: per clip, a midframe + auto scores (sharpness / brightness / shake / motion) + tags (subject, action, setting) from contact sheets.
- **Usage ledger:** every shipped video records which clips it used. "Fresh, steady, bright cat-eating shot, never used" becomes a query, not a memory exercise - footage variety enforced by system, and the pre-render variety board generates itself.

### Phase 4 - Close the loops
- **VO retrain (10 minutes, permanent lift):** one hyped, energetic training take for the voice clone - the ONLY thing that raises the VO ceiling once settings are maxed. Then A/B the newer expressive TTS models against your current one. Meanwhile: generate 3 takes per line, score energy (Phase 1 tooling), keep the best.
- **Retention ritual made real:** after each post, drop the IG Insights retention screenshot into a per-video folder; map drop-offs to timeline beats; append the lesson to this doc as a rule.
- **Codify as an agent skill** so every video session auto-loads this doc, the per-format checklist, and the screening-room gate; the self-learning loop (§9) appends there.

**Explicitly out of scope:** generative footage (Runway etc.) - real footage only. The quality gap is craft + verification, not synthesis.

**Only-human dependencies:** (1) the hyped VO training take, (2) the Remotion license decision, (3) retention screenshots after each post.
