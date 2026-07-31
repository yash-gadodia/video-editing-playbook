# The Editing Rulebook

The mechanical rules for cutting a short-form video, synthesized 2026-07 from: frame-by-frame decodes of downloaded reels (see [case-studies/](case-studies/)), a 3-agent research sweep of top pet brands + pet creators + retention-editing practice, and direct field feedback from a full-time content creator on our own cuts.

**Evidence tiers** - every rule is tagged:
- `[OBSERVED]` measured in reels we downloaded and cut-detected ourselves (strongest)
- `[CRAFT]` practitioner consensus technique (Hormozi/MrBeast-school editors, studio writeups)
- `[STAT]` a number from marketing sources - treat as hypothesis; our adversarial research killed most of this genre (see [RESEARCH-instagram-growth.md](RESEARCH-instagram-growth.md))

## 0. The law above the rules
`[OBSERVED]` **Premise > polish.** The two biggest reels we decoded (5.8M + 4.6M views on a 6K-follower account) have zero VO and near-zero editing - a confession and a transformation arc carried them. The same account's beautifully edited product reels: 50-700K. Spend 80% of effort on premise + hook, 20% on the cut. Editing amplifies; it never rescues.

## 1. Hook (0-3s)
1. `[FIELD]` The hook formula: `[I/WE] + dramatic verb + specific number + open loop` - "I LOST $600 ON MY OWN ORDER, here's why". First person, stakes, a number.
2. `[FIELD]` Every hook must contain at least one of: **a number, a loss, a confession, a contradiction**. None = rewrite.
3. `[OBSERVED]` Open-loop pinned caption ending in ":" that only resolves in the post caption = dwell-time machine (the 4.6M reel). Needs genuinely spicy content; use sparingly.
4. `[OBSERVED]` Pinned context banner top-center for first ~10s tells mid-scrollers what they're watching. Below the top-18% notch zone.
5. `[CRAFT]` Cold-open mid-action; never open on a logo, an establishing shot, or a greeting.
6. `[CRAFT]` Fragment the first sentence - cut to the next shot mid-thought so the brain follows the incomplete pattern.
7. `[FIELD]` **No jargon in the hook.** If anyone has to ask what a word means, the scroll is already gone. Technical terms live on receipt surfaces (site screenshots, tables) where they signal expertise; the hook gets playground words ("cats NEED meat. period." beats "obligate carnivores"). Field-tested: the founder himself asked what the fancy word meant.

8. `[OBSERVED]` **Average play time on our reels is 4 to 15 seconds against runtimes of 38 to 76 seconds.** Measured across a full account in Meta Business Suite, not inferred. Whatever the piece is *for* has to happen inside the first ten seconds; end cards, CTAs and pay-offs placed at 0:30 are being seen by almost nobody. Front-load the pay-off and treat the tail as a bonus for the few who stay.

## 2. Pacing
1. `[OBSERVED]` VO-driven reels: average shot 1.2-1.5s (measured: 1.23-1.35s across kaiandjia's product reels; our old default of ~2.5s is too slow).
2. `[OBSERVED]` **Cluster your cuts.** Pace is rhythm, not a constant: the gabrieljudah reel machine-guns 8 cuts in 6s on the receipts beat, then holds 3-4s shots during the one key explanation. Fast where evidence stacks, slow where the idea lands.
3. `[OBSERVED]` Caption-driven photo-dump (no VO): ~1.2s per image, one caption line per image.
4. `[CRAFT]` Visual change every 3-5s minimum even inside a single talking-head take: punch-in, caption pop, overlay animation, or location reset.
5. `[OBSERVED]` Location/framing reset mid-monologue (same VO sentence, new backdrop) adds perceived pace without touching audio.
6. `[CRAFT]` No dead frames: nothing on screen may sit unchanged longer than ~5s (talking head) / ~2s (b-roll montage). Kill breaths and pauses.
7. `[FIELD]` **Speech density is the cheapest lever you have.** On the best talking-head cut we have shipped, 22.1s of a 23.4s timeline is someone actually talking (95%). The 38.3s raw take contained a 10.1s dead-air gap where the founder stopped to read his notes, plus ~4.7s of inter-line pauses. All of it went. Raw takes are routinely 40-60% air; measure the ratio before you start decorating the edit.
8. `[OBSERVED]` Length serves the story: 13.5s and 68s both went 4M+. Cut to the story's natural end, then delete every second that doesn't earn its place. Ignore "optimal length" folklore.

## 3. Cuts (what "clean" means)
1. `[FIELD]` **Drive cuts from a word-level transcript.** Whisper with word timestamps gives every word a start and end; pick in/out points from those numbers and a clipped consonant becomes structurally impossible. This also makes the edit reviewable as text before you render a single frame.
2. `[FIELD]` Cut ON word boundaries, never mid-breath. No residual frames from the previous clip. No sloppy audio overlap across cuts.
2. `[CRAFT]` J-cuts and L-cuts for VO flow: let the next line's audio start before the video cuts (J), or the video move on while the line finishes (L). Hard-cutting both together every time reads amateur.
3. `[CRAFT]` Audio-first editing: place cuts on audio peaks/beats, not arbitrary frames. Extract the waveform, snap cuts to it.
4. `[CRAFT]` Punch-in (5-10% scale jump) instead of a new angle to break up a single take; on the beat.
5. `[OBSERVED]` Face returns to camera for the ONE line that matters most ("this is the part that really matters"). Emphasis = presence, not volume.

## 4. Captions & graphics
1. `[OBSERVED]` Caption pops of 2-5 words, replaced on nearly every phrase - never full sentences (gabrieljudah). Bold, white, drop shadow, centered ~65-70% height.
2. `[OBSERVED]` Story format: 2-line sentence-case captions, one per shot (kaiandjia photo-dump).
3. `[OBSERVED]` Numbered step stickers ("02 CONNECT..." white sticker, colored badge, slight rotation) persist through each step of a how-to.
4. `[OBSERVED]` Live counter/progress-bar overlay animating during talking-head beats (credits bar 38→81→100) gives the eye a moving target. Bon Pet analogues: orders shipped, kg cooked, reviews count.
5. `[OBSERVED]` Every enumerated word gets its own visual: VO says "2nd, 3rd, 4th draft" → screen shows drafts 2, 3, 4.
6. `[CRAFT]` Kinetic typography synced to VO is the current standard; animate titles and CTAs, leave body captions simple.
7. `[CRAFT]` ~85% watch muted: the video must work with sound OFF. Captions everywhere, visual proof over spoken claims.
8. `[FIELD]` **Screenshot web proof at a MOBILE viewport, never desktop.** A desktop-width capture dropped into a 1080x1920 frame is an unreadable postage stamp. Shoot the page at ~430px CSS width (device scale 3) so it reflows tall, then crop a section: it fills the frame edge to edge with type you can actually read. This is the difference between a proof beat that works and one that is decoration.
9. `[FIELD]` **Full-frame proof cutaways should be L-cuts.** Land the cutaway exactly on the words that describe it and let the speaker's audio run underneath unbroken. It reads as evidence appearing mid-sentence rather than as a slideshow interrupting the video. Two cutaways of ~2s each inside a 23s cut was the right dose.
10. `[FIELD]` Sample the screenshot's own corner pixel for the card background colour. A near-white page crop on a brand-cream card leaves a visible rectangular seam that reads as sloppy compositing.
11. `[FIELD]` **Clamp each subtitle's hide time to the next subtitle's show time.** Adjacent caption pills with independent fade-in/out windows will render on top of each other for a few frames. Mine did, and only a frame contact sheet caught it.
12. Safe zones (house rule, kept): nothing in top ~18% of frame; overlays never block faces.

## 5. Sound
1. `[CRAFT]` Ducking: music -12 to -18dB under speech; SFX -3 to -6dB under VO. Felt, not heard.
2. `[CRAFT]` SFX on cuts (whoosh/pop/click) sparingly, on beat - transitions feel "clean" largely because of sound.
3. `[OBSERVED]` No-VO story reels: ironic/emotional trending-audio pairing does the emotional captioning (happy couple + "now that you're gone" lyric).
4. `[CRAFT]` One second of near-silence right before the single most important line.
5. `[FIELD]` **Silent clips feel bare.** Footage with no diegetic sound (muted UGC, stills) exposed under bare VO reads unfinished. Default to a music bed when the footage itself is silent. UPDATED house rule: music MAY bake in when rights are cleared (your own royalty-free library, e.g. CC-BY tracks with a caption credit, or a platform music allowance for your account). Trending/uncleared audio still gets layered in-app, never baked.
   - Bed it as ONE continuous ducked track, never patchwork music only on the silent clips - patchwork reads as broken audio.
   - Duck the bed hard (near-zero) under any diegetic ASMR beat so the natural sound stays the star, and fade the bed out over the last ~1.2s.
   - Field-tested bed level: ~0.06-0.08 gain under VO. Our first default (0.12) was immediately flagged as too loud by the founder.
6. `[FIELD]` **Engineer diegetic gaps by splitting the VO.** TTS voices can't hold a long pause. Generate the VO as two files (A ends on the "sound on" line, B resumes after), place B at `A_end + gap`, and let the clip's natural sound own the gap. Word-timestamp anchors still work per part with the offset added.
   - **Level-match the gap.** "Full volume" is only right for genuinely quiet ASMR sound (soft eating, pouring). Noisy room audio at 1.0 after a ducked section is a jarring wall - lift it to ~0.4 instead. Verify with volumedetect: the gap should sit +1 to +3dB above its neighbors, not +8.
7. `[CRAFT]` **Natural/diegetic sound is not music - keep it.** Teasers and food/ASMR reels often need NO VO; the footage's own sound (broth pouring, a cube popping, a furkid crunching/lapping) is the hook and is copyright-safe to bake into the master. Distinguish: strip music, keep diegetic sound. (`REEL_AUDIO=1` in `lib_reel` keeps clip audio; stills/muted clips get a silent track so the concat stays uniform. The founder can still layer quiet trending audio in-app on top, or leave it pure ASMR.)

## 6. Structure (the retention skeleton)
1. `[OBSERVED]` The AI-demo/how-to skeleton (gabrieljudah, 122s): promise → free/easy → "but here's the catch" → most-people's-mistake → the opposite → receipts ("that video went viral", counts on screen) → numbered steps → quotable aphorism → comment-keyword CTA.
2. `[OBSERVED]` The story skeleton (kaiandjia, 5.8M): chronological adversity arc in captions over real archival footage; the business is the PAYOFF of the personal story, never the topic.
3. `[CRAFT]` Mini open-loops in the body ("I'll come back to this"); attention reset every 20-30s (twist, cutaway, sound spike).
4. `[CRAFT]` Loop-back endings (last shot flows into the first) inflate completion via replays.
5. `[OBSERVED]` Receipts beat: show real numbers on screen (view counts, revenue, order counts) during the fastest-cut section.

## 6b. What actually made the difference (measured, not felt)

1. `[OBSERVED]` **Shares separate a hit from a flop, and nothing else comes close.** Across one account's recent output, the single reel that reached ~3x follower count took 18 shares and 227 interactions; everything the brand produced itself took 0 to 2 shares and 3 to 16 interactions. Shares are a confirmed ranking signal, so this is a mechanism and not a mood. Before rendering, ask the concrete question: who forwards this to whom, and what does sending it say about the sender? If there is no answer, the edit will not save it.
2. `[OBSERVED]` **Carousels are the save format; reels are the reach format.** A static carousel with under 1,000 views collected 6 shares and 5 saves, more than any reel on the account. Put reference material (numbers, comparisons, receipts) in carousels and motion-dependent storytelling in reels, rather than forcing everything into video.
3. `[OBSERVED]` **Reach does not convert to follows on its own.** A reel at ~3x follower count produced one follow. If follower growth is the goal, the ask has to be built into the piece; volume alone does not do it.
4. `[FIELD]` **Pull the numbers from the platform's content table, not the public grid.** Logged-out grid counts were 35% low against the same post's logged-in figure, and the grid hides shares, saves, watch time and average play time entirely. The deeper columns are where the lesson is.

## 7. UGC-sourced edits (compilations, testimonial reels)
1. `[FIELD]` **QA every chosen clip's baked-in text for creator promo/referral codes AND third-party brand handles BEFORE building.** Customer story reposts often carry the creator's personal discount code, or a tag of another brand they feed alongside yours (e.g. a kibble-mix combo), baked into the frame. Either one can land on exactly the wrong beat of your script. Cropping rarely hides it cleanly - replace the clip instead.
2. `[FIELD]` Visible usernames/story stickers in UGC are receipts, not clutter - keep them. They ARE the authenticity. Place your overlays around them.
3. `[FIELD]` Caption y-position is per-clip, not global. A y that clears one clip's subject sits on the next clip's face. Split a caption into windows with different y per segment when the subject moves (and re-check every window against faces - a top-of-frame default is not an answer).
4. `[FIELD]` Check your display font's glyph coverage before shipping stickers - symbol glyphs (e.g. ★) silently render as nothing in some display fonts. Spell it out ("4.8/5") or render the symbol as an emoji layer.
5. `[FIELD]` Survey footage by contact sheet (1 mid-frame thumb per clip, grid, indexed), shortlist, then verify motion with 3-frame strips per candidate. Never pick from filenames.

## 8. What we explicitly do NOT import (quarantined folklore)
Our adversarial research (200+ agents, ~190 claims, 6 survivors) killed the marketing-blog versions of: trending-audio reach multipliers, micro-influencer superiority, optimal posting cadence, format-type preference stats, "67% more trusted" UGC numbers. The verified fundamentals remain: **watch time, completion, replays, shares** are the ranking signals; read first-party retention data, not listicles.

## 9. Source prep (do this before a single cut)

1. `[FIELD]` **Check the source colour space first.** `ffprobe -show_entries stream=color_transfer,color_primaries`. If it reports `arib-std-b67` (HLG) or `smpte2084` (PQ), the file is HDR and feeding it straight into ffmpeg will wreck the colour. Modern phones record HDR by default, so this is now the common case, not the exotic one.
2. `[FIELD]` **Two ways to get HDR wrong, both shipped by me in one session.** (a) Decode it naively: ffmpeg ignores the tags, reads the HLG curve as if it were gamma and BT.2020 values as if BT.709, and you get a flat, washed-out, undersaturated image. It looks "fine but dull", which is exactly why it slips through review. (b) Hand-roll an HLG to BT.709 3D LUT: the classic bugs are applying the HLG OOTF at gamma 1.2 (that is the *1000-nit* system gamma) on top of the display gamma, which double-counts system gamma, plus a full BT.2020 to BT.709 matrix on content that is effectively near-709 gamut. Warm tungsten skin and walls go orange. The review verdict on that render: "why so red? looks weird like a bad filter".
3. `[FIELD]` **The fix: let the OS tone map, do not reimplement it.** On macOS, pre-transcode to an SDR BT.709 master with AVFoundation, then run the entire ffmpeg pipeline on that master. `templates/tosdr.swift` does it in about 20 seconds for 38s of 4K, keeps audio and exact timing, and bakes in the rotation so there is no display-matrix side data to handle downstream. The usual `zscale=t=linear,tonemap,zscale=p=bt709` recipe is unavailable on ffmpeg builds compiled without libzimg, and that absence is precisely what tempts you into the hand-rolled LUT. Do not take the bait.
4. `[FIELD]` **Get a ground-truth reference frame before judging any grade.** `AVAssetImageGenerator` returns a system-tone-mapped still, the exact thing the OS video player shows. Render your version beside it and LOOK. Do not trust "mine looks richer than the raw decode" as evidence of correctness; richer was the failure mode. `templates/ref_frame.swift`.
5. `[FIELD]` **A numeric fit that bottoms out at the edge of your parameter grid is telling you the approach is wrong, not that the parameters need tuning.** I swept OOTF gamma, primaries matrix, exposure and desaturation against the reference; the best fit still had ~27/255 mean absolute error and kept pushing toward the grid boundary. That was the signal to stop tuning and delegate the transform.
6. `[CRAFT]` Transcribe the raw take at word level before planning cuts. The transcript, not the waveform, is the edit decision list for anything with speech.

## 10. Interview & collab formats (the highest-leverage shape we have found)

1. `[OBSERVED]` **Stacked split-screen interview.** Guest fills the top pane, host the bottom, both talking heads, no empty frame. The listener's face is doing real work: it gives the scroller a reaction shot and a reason to stay. Observed on a collab interview of our founder by a pet-media account; it is the same shape used across the interview-clip economy.
2. `[OBSERVED]` **Yellow word-by-word captions at the seam between the two panes.** High-contrast yellow reads on skin, walls and clothing alike, which is why it is the default in high-retention interview clips. Worth A/B testing against a brand-coloured caption, because brand colours are chosen to look correct, not to survive a 4-inch screen at arm's length.
3. `[FIELD]` **One long interview is a series machine, not one video.** A 7-minute founder interview cut at question boundaries yielded 10 self-contained clips (0:13 to 1:14 each). Each answer already opens with its own question, which IS the hook. Film once, ship for weeks.
4. `[FIELD]` **Question design decides whether the answers are usable.** The questions that produced shippable clips all forced a confession or a contradiction: "if you started over, what would you change", "what was the biggest problem", "how did you get your first 100 customers". The ones that produced flat answers were positional ("how do you think about competitors"). Write questions that can only be answered with a loss, a number or an admission, per rule 1.2.
5. `[FIELD]` **Answers that break the expected script travel furthest.** The strongest lines in our own interview were the ones that refused the premise: "I don't think the business has actually taken off, we're just getting started", and naming the biggest mistake as something the founder chose to do. Prompt for those explicitly, they rarely arrive unprompted.
6. `[CRAFT]` **Plant an open loop inside the interview.** Two separate answers teased an upcoming transparency drop ("stay tuned, we are publishing every single dollar"). That converts a one-off interview into an on-ramp for the next launch.
7. `[FIELD]` **Always publish partner content as a collab post**, not a repost. It lands on both grids and both follower feeds. In our own data, collab posts run 1.5 to 2.6x median while brand-owned announcements run at or below it.
8. `[FIELD]` **Ship the raw interview to the partner as frame-accurate clips plus a word-level transcript and a shotlist.** They edit faster, they credit accurately, and you keep an identical set to cut your own versions from later.

## 11. Showing a real document (redaction is a format, not a chore)

1. `[CRAFT]` **The redaction IS the hook.** A blurred real document signals "this exists and I am choosing what to withhold" in a way a clean designed graphic cannot fake. Withholding reads as more honest than showing nothing, and more credible than a mockup. The reaction to our own build of this was the strongest we have had.
2. `[FIELD]` **Redact default-deny: blur the whole frame, then restore only the regions you have explicitly cleared.** The intuitive way round (list the regions to blur) leaks. A first pass over ten spreadsheet tabs missed the summary rows, because they sat outside every rectangle we had thought to name.
3. `[CRAFT]` **Keep the labels sharp and kill the values.** Row and column headings readable, figures blurred. The viewer sees *what* is tracked without the numbers, and the surviving structure is exactly what makes it read as genuine rather than staged.
4. `[CRAFT]` **Number the versions.** A montage of near-identical screenshots is boring. The same montage labelled V1 through V7, each with one line on what that version tried, becomes a progress narrative with a destination. The label carries the meaning, so individual cells never need to be legible.
5. `[FIELD]` **Read the margins of every screenshot before it ships.** Working documents carry things the story does not need: third-party ad spend, vendor and contractor names, competitor names. One tab in our own set had all three parked in unused columns. Blur by region, not by data type.
6. `[CRAFT]` **End on the one thing you ARE publishing.** After a run of redactions, the single unblurred artefact is the emotional pay-off.

## 12. Rendering integrity (the failures that ship silently)

1. `[FIELD]` **Never `zoompan` a static card.** It rounds its crop offset to whole INPUT pixels each frame, so a slow push-in on a still oscillates about a pixel and reads as shake. Supersampling the source 2x halves it but does not remove it (measured: 5 one-pixel reversals across 43 frames). Animate opacity instead: `scale=W:H:flags=lanczos,fps=30,setsar=1,fade=t=in:st=0:d=0.30` over a `-loop 1 -t DUR` still. Alpha cannot quantise position, so shake becomes structurally impossible rather than merely reduced.
2. `[FIELD]` **`zoompan`'s `d=` counts output frames PER INPUT FRAME.** Hand it a looped still and every input frame spawns a full `d=` run, so each card silently becomes minutes long and `-shortest` truncates the timeline to the first one. Feed exactly one image, no loop, and cap with `-frames:v N`.
3. `[FIELD]` **Join segments with the concat FILTER, not the concat demuxer.** The demuxer assumes every input already shares codec parameters and silently mistimes them when they do not. A clip that inherited 44100 Hz from a phone source, joined to segments encoded at 48000 Hz, held its last frame for ~1s at the seam. The filter re-normalises fps, scale, sample rate and channel layout per input, so the whole class of bug disappears.
4. `[FIELD]` **Pin `-ar` and `-ac` on every intermediate encode.** Sample rate is inherited from the source when unset, so segments built at different moments drift apart with no warning. Decide one canonical spec (resolution, fps, pixel format, sample rate, channel layout) and force it on every intermediate.
5. `[CRAFT]` **Assert duration after every join.** Compare the output against the sum of its parts and fail loudly past a small tolerance. The freeze above was sitting in the numbers (10.97s expected, 11.97s actual) long before anyone saw it on screen.
6. `[FIELD]` **Verify motion numerically, never by eye.** For frozen frames, decode at ~10fps and flag runs where consecutive frames differ by near zero. For jitter, cross-correlate consecutive frames: try a shift of -1, 0 and +1 px per pair and check which alignment minimises the difference. All zeros means genuinely static. Edge-threshold tests give false positives on anti-aliased curves, which is how a card that is provably static can still look like it is moving.
7. `[FIELD]` **Display fonts carry no emoji glyphs, and PIL drops them silently** - no tofu box, just nothing where the emoji was. Either omit emoji from rendered cards or draw them from the system colour-emoji font with `embedded_color=True`, which accepts only fixed strike sizes. Emoji in the post caption are unaffected. A grey paw on a dark brand colour reads as a smudge regardless; let the logo carry it.
8. `[CRAFT]` **Auto-fit caption text to a safe width.** A point size that fits one line will overflow the frame on the next. Shrink until it fits, then wrap.

## 13. Ending a video

1. `[FIELD]` **Every cut ships with a closing CTA card, memes included.** Roughly 1.5 to 2s: logo, a follow line, the site. A video that simply stops on its last content frame feels abrupt and wastes the attention it earned.
2. `[CRAFT]` **Let the bed carry through the card.** Cutting audio dead at the seam is what actually makes an ending feel broken, more than the visual.
3. `[FIELD]` **The CTA is closure, not the mechanism.** Rule 1.8 measured that almost nobody reaches the tail, so the card is for the few who stay. Never park the pay-off there, and never let "there is a CTA at the end" substitute for building the ask into the first ten seconds.
4. `[CRAFT]` **Soft CTA only.** Follow, or the site. Codes and hard offers on an end card turn a shareable piece into an ad, which costs more reach than the offer wins.

## The pre-render gate (run before every render)
1. Hook: number/loss/confession/contradiction present? Stranger-stops-scrolling test passed?
2. Premise: would this be interesting with ZERO editing? If no, fix the premise first.
3. Pace: VO shots ≤1.5s avg, cuts clustered around receipts, no frame unchanged >5s.
4. Cuts: word-boundary cuts, J/L where VO flows across, no residual frames.
5. Captions: ≤5 words, out of notch zone, never on a face.
6. Sound: music ducked (bed dipped near-zero under ASMR beats), works muted, silent footage has a bed (bare = unfinished).
7. Structure: open loop in first third, receipts shown not told, comment-bait or loop-back ending.
8. House QA (from PLAYBOOK.md): no repeated footage, stills static, real labels, coverage/frozen-frame/chopped-word checks.
9. UGC: no baked promo/referral codes or third-party brand handles in any chosen clip; overlay y checked per clip against faces; font glyphs verified.
10. Real-world numbers on screen (ratings, review counts, order counts) re-verified against their live source at build time - brand stats drift and a stale counter in a receipts beat undermines the whole receipt.
11. Source colour: if the raw file is HDR (`arib-std-b67` / `smpte2084`), was it converted through the OS tone mapper first? Was the render compared against a system reference still?
12. Speech density: what fraction of the timeline is someone talking? Under ~90% on a talking-head cut means there is still air to remove.
13. After shipping: push the session's new learnings to this repo, same session. The rulebook only compounds if every build pays into it.
14. Rendering integrity: duration asserted against the sum of parts after every join? Frozen-frame scan run over the whole timeline? Any move on a still proven static by cross-correlation rather than by watching it?
15. Ending: CTA card present, bed carrying through it, and the ask also made inside the first ten seconds?
16. Redaction (if any real document is on screen): built default-deny, margins of every screenshot read for third-party names and spend, labels sharp and values killed?
