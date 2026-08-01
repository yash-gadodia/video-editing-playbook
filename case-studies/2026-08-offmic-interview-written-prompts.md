# The off-mic interview: cut the question, write it instead

**Build:** a 42s interview cut with two teenage part-timers at a pet expo, shot on one phone, one static angle, one take of 1m51s. Brief from the founder: *"make a video about them, their experience, u can take footage from the folder if needed, dont over edit it ya, keep it genuine."*

This is the counterweight to most of the rulebook. Almost every rule in [EDITING-RULES.md](../EDITING-RULES.md) pushes toward faster, tighter, denser. "Keep it genuine" is a instruction to stop short of that, and the interesting question is *which* rules still apply when polish is explicitly not wanted.

## What "don't over-edit" actually meant

Kept: word-boundary cuts, subtitles, a static punch-in, a quiet bed, the closing card.

Dropped: the 1.2-1.5s cut rhythm, VO, kinetic captions, a scripted hook. The cold open is the two of them giggling through a mic test - literally the throwaway clip named `funny-test.MOV`. It signals "unpolished" inside one second, which is the whole premise, and no designed hook card could have done the same job.

The jump cuts between answers were left visible. In a single locked-off shot they read as an honest interview rather than as sloppiness, and hiding them would have cost the thing its texture.

## The correction that mattered: the interviewer had no mic

v1 played each question as audio, cut from the take. The founder's note:

> *"when i ask the qn, you dont need to show that part, just the answer with the question prompt. u gets? like at 4s when i say 'what are ur names' - i have no mic on, it doesnt need to be included, just show the answer itself, and u can add the qn as a fixed prompt or smth"*

Every question became a small pill pinned at the top of frame, held for the whole answer, and all interviewer audio was cut. Effects, in order of how much they surprised me:

1. **Runtime went 52s to 42s**, and every second removed was material nobody could hear anyway.
2. **The prompt is a better artefact than the question was.** It persists. A viewer who joins mid-answer can still read what is being answered; a spoken question is gone the instant it is said.
3. **It killed a whole class of transcription risk.** Three questions had been reconstructed from muffled audio and were about to ship as quoted speech. Once they became written prompts, they were design copy - and could be phrased shorter and more casually than they were actually asked: "funniest customer so far?", "still studying?".

Generalised into rules 10.9 and 10.10. It applies to any run-and-gun interview where only the subject is mic'd, which is most of them.

## Show the noun

Two more notes, same session:

> *"at 22s when she says - the dog keeps jumping on me to get food from the plate - SHOW it"*

> *"can u add in a doberman cutout or smth? find online"*

Both are the same instruction: when the speaker names a specific concrete thing, that is a shotlist. The first was covered from the take itself - the same camera had panned to a dog bouncing up on its owner three minutes later, which is a literal illustration of the line. The second did not exist in any archive, so it came from a licensed stock photo, background removed with rembg, given a cream outline, and dropped in on the word "doberman".

Two things learned compositing it:

- **Cutouts must render UNDER the caption layer.** Drawn on top, the dog covered its own subtitle and read as a sticker pasted over the video. Drawn first, with the caption pill sitting on its legs, the same asset reads as an object standing in the scene. Identical pixels, one line of ordering, completely different perception.
- **Keep the whole subject inside the frame.** The first placement ran the dog off the left edge to buy clearance from a face. Reviewed at full zoom, the clipped chest was the first thing spotted. Shrinking it slightly and bringing it fully inboard fixed it - a partial cutout reads as a mistake in a way a smaller complete one never does.

The general form is rule 4.13: own footage, then the archive, then licensed web. Skipping a visual because you do not happen to own it is the lazy default.

## Transcription is not a solved step

The single whisper pass over the take contained a hallucination that would have shipped: a 24-second stretch with no clear speech came back as one confident segment reading "I thought I was walking home home home home..." roughly sixty times, timestamps and all. It sat directly on top of the best exchange in the interview, which was recovered only by re-transcribing that window in isolation.

Separately, one line resisted four passes - "studying dreddy cooked" / "studying generally cooked" / "saying ready cooked" / "studying Jaday cooked". Isolating and cleaning the snippet, slowing it to 0.7x and decoding at two temperatures narrowed it, but not to certainty. It shipped flagged to the person who was in the room rather than as a confident quote.

Subtitles are attributed speech. A mis-heard verb is a factual error about what someone said, not a typo. Rules 9.7 and 9.8.

## The cheapest verification available

Re-transcribe the finished render and diff it against the intended caption list. It proves in about two minutes that no cut clipped a word, that every planned beat survived the concat, and that nothing meant to be removed is still audible. It caught nothing this time, which is the point - it is how you find out.

## Plan the archive pull first

Time was lost to an assumption. Asked for jumping-dog footage, the obvious move was the event archive - 329 clips from the right event, sitting in a cloud-synced folder, all listing real byte sizes. All dataless stubs. Materialising managed roughly 25 clips in several minutes even 8-way parallel, and the one promising result turned out to be a 5-frame Live Photo. The shot that shipped was in the original take the whole time.

Two habits from that: start any archive pull in the background at the top of the session, and check `st_blocks` before believing a file listing. Rule 9.9.
