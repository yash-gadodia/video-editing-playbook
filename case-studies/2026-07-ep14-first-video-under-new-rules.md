# Build log: the first reel produced under EDITING-RULES.md

Ep14 "sous vide 80°C vs kibble 150°C" (Fur the Record series), built 2026-07-07 - the first video where the evidence-tiered rulebook was applied from scratch. What the gate changed, and two new reusable techniques.

## How the rules shaped the build
1. **Hook formula applied**: "kibble: cooked at 150°C" - number + contradiction in second 0.2, spoken AND stickered. Old draft ("how we cook it") would have failed the number/loss/confession/contradiction test.
2. **Premise-first**: the video is a receipts-backed industry contradiction (heat kills nutrients → vitamins get sprayed back on → there is a patent), not a process tour. The process footage serves the argument.
3. **Cut clustering, measured**: theirs/receipts beats hold 1.8-3.2s (readable), ours-process section runs 9 shots in 11.5s (1.28s avg) - matches the observed 1.2-1.5s VO-driven benchmark without being uniform.
4. **Fact-check gate**: both on-screen numbers were adversarially verified BEFORE the VO was generated (extrusion barrel 110-150°C; post-extrusion vitamin coating standard, US patent 9,585,412). The claim survives because a skeptic can google it.
5. **VO pacing reality**: 92-word script → 25.7s at speed 1.16. Rule of thumb confirmed: ~3.5 words/sec for the cloned founder voice. Script to ~90 words for a sub-30s reel.

## New reusable technique: the patent receipt
For any "industry secret" claim, screenshot the PRIMARY SOURCE (Google Patents page: title + abstract + patent-number card), restack the crops vertically with PIL, and show it as a static receipt while the VO says "for real". Authenticity beats any motion graphic, costs 2 minutes, and is legally safer than showing a competitor's bag under a process claim (bags also mislead: canned food is retorted, not extruded - never pair wet-food imagery with extrusion claims).

## Pipeline gotchas logged
- Apple Color Emoji via PIL now requires its fixed strike sizes (160/96/64...) - arbitrary sizes throw "invalid pixel size". Try-fallback loop + bbox-crop + resize.
- `apad` + `-shortest` leaves a black tail; use explicit `-t <video_end>` on the final mux instead.
- ElevenLabs `/with-timestamps` char alignment → word start-times drive BOTH segment durations and caption enable-windows; captions land on word boundaries by construction (the "clean cuts" rule, automated).

## Pre-ship verification state
Deterministic checks passed (duration 28.0s exact, receipt legibility frame-checked, no within-video footage reuse, safe zones respected). Flagged for human playback: VO energy/feel, cut rhythm in motion, and two kibble-bowl clips that belong to a clip family used in an older reel (cross-video reuse minimized but not zero).

## v2 iteration (founder review of v1)
Feedback: voice slightly robotic, one weird mid-phrase pause ("Fur... the record"), pacing approved, hook "kind of sucks u in", wants more footage variety across episodes.
1. **Voice-clone naturalness**: stability 0.30/style 0.50/speed 1.16 reads robotic. The energy settings (stability 0.14, style 0.68, speed 1.10) are the better default for founder VO. Slower speed lengthens the whole VO (~+12%%) - re-derive every segment + caption window from the fresh word timestamps.
2. **TTS pause bug + fix**: unusual multi-word phrases (brand puns like "Fur the record") make the clone insert a sentence-break pause mid-phrase. Hyphenate to force connection: "fur-the-record?". 
3. **Deterministic pause QA**: parse the timestamp JSON and flag any intra-sentence word-start gap >0.8s. The agent can't hear; this check catches what ears would.
4. **Footage-variety debt is real**: by video ~7 on the same b-roll library, the founder notices repetition. Maintain a per-reel ledger of which NAS footage FAMILIES have been used, and require each new reel to pull at least one never-used family. (Our unlock: the founder's own dog's feeding-POV folder - 21 fresh clips, instantly the most charming shots in the cut.)
