# Build log: ep15 founder-story photo-dump (the megahit-format attempt)

Applied the kaiandjia 5.8M formula end-to-end for The Bon Pet, 2026-07-07. Template: [templates/photodump_story_build.py](../templates/photodump_story_build.py).

## Format decisions (all from the case-study evidence)
- **Caption-driven, zero VO** - sidesteps voice-clone quality entirely; the captions ARE the narration (founder first person, "Nic and I").
- **Confession hook with a number**: "We've taken $0 out of our own pet food brand. On purpose." - number + confession + open loop, and it's TRUE (brand canon; never contradict).
- **Arc**: hook → origin → adversity artifact (a real broken-table photo beats any stock "struggle" shot) → zero-customers stakes → the bet (free packs) → cost ($9/pack, real) → emotional pivot ("look at these faces") → receipts (4.8★, AAFCO, open formulas) → mission → follow. Business facts land as the PAYOFF of a human story.
- **One photo per caption beat**, ~1.6-2.4s each (1.6s for montage runs, 2.2-2.4s where text is heavier). Photos STATIC; only real videos move.

## The SFX kit (synthesized, license-free)
User kept asking for "the ding" - viral sound design is a mandatory layer now. 10 sounds synthesized in pure ffmpeg (aevalsrc/anoisesrc), saved as a reusable kit: ding, bell, boom, riser, camera shutter, sparkle, cha-ching, pop, whoosh, tick.
Design grammar used: **boom** under the hook, **shutter** on every photo cut (the photo-dump signature), **ding** on the bet reveal, **cha-ching** on the money line, **pop** run through the dog montage, **riser** 1.45s before the payoff beat, **sparkle** on the stats, **bell** on the mission line. Volumes 0.3-0.65, mixed with amix normalize=0, apad to video end. Trending music still gets added in-app ON TOP.

## Animation grammar
- Captions slide up 50px and settle over 0.22s (ffmpeg overlay y-expression with if(lt(t,...)) - no Remotion needed for this format).
- Escape commas as \, inside overlay expressions.
- Contact-sheet QA false positive: between(t,a,b) windows that share a boundary double-render for exactly 1 frame - invisible in playback, looks like caption overlap on a sampled sheet. End windows at t1-0.034 if it matters.

## Sourcing lesson
NAS index (metadata CSV with an online_only flag) made casting fast, BUT the flag goes stale - files evicted since indexing re-hydrate on read and a "quick thumbnail" of five 500MB MOVs can time out. Filter candidates by size + local flag, thumbnail small files first, copy selects into the build dir before cutting.

## v3: the amix silence bug (founder reported "no sound")
`amix` treats an input that ENDS as a dropout and ramps the mix down - with 15 short adelay'd SFX streams, everything after the first sound faded to digital silence even though volumedetect showed a healthy max (the boom). **Rule: pad every SFX stream to the full video duration (`adelay,volume,apad=whole_dur=END`) BEFORE amix, then `amix=duration=first:dropout_transition=0:normalize=0` + a limiter.** Verify with per-window RMS (`astats=reset=1`), not just volumedetect max - a single loud hook masks a dead track.
