# Case study: Thariq's code-driven video editing (Anthropic)

**Source:** Thariq Shihipar (Anthropic, Claude Code team), live-tweeting on 2026-07-08 as Claude/Fable edited his AI Engineer talk. Thread: https://x.com/trq212/status/2074617786408845774 . Library is closed-source for now ("just a bunch of scripts and remotion assets", may open-source).

## What he did
Dropped 59GB of raw talk footage (4 videos: multiple on-stage camera takes + deck-cam) plus his **HTML deck** into one project folder, and had the agent edit it into a finished video **entirely through code**, no timeline editor. Steps he showed:

1. **One project, all inputs together** (`@projects/aie-talk`): audio, several on-stage takes, deck video, deck as HTML.
2. **Transcribe** with word-level Whisper.
3. **Composite** slides + speaker-cam, tracking his on-stage position.
4. **Generate animations** from the HTML deck (section intros, dynamic motion).
5. Auto-cut **YouTube shorts** from the transcript.
6. Render **low-res previews**, review, iterate, full render last.

## His architecture (from the screenshots)
`claude-video-editor` = Python scripts + Remotion (React) components, orchestrated by Claude:
- `transcribe.py`: word-level Whisper, OpenAI JSON schema `words[] = (word,start,end)`, **incremental cache** ("new clips only does the new work"), pluggable whisper backend, `transcript-fixes.json` correction layer (Whisper silently drops words).
- Remotion `.tsx`: `FootageWithCues`, `OverlayLayer`, `anim`, `theme`.
- Scripts: `cut.py`, `snippet.py`, `srt.py`, `words.py`, `anchors.py`, `audit.py`, `new_project.py`, `_common.py`.

## His prompt (the real lesson)
> "Edit this into a single high quality video. We'll iterate, so **break it into composable building blocks like transcripts, UI elements, JSON things** so things are easy to move around. Be creative, it's a technical talk so use code generation + UI. **Use subagents when doing ambitious work.** Reuse the flow from @projects/acm-talk. I want specific cuts/previews **without compiling the whole thing**. Do the groundwork, then come up with different ideas of how to cut it and **do a few small renderings** to show it."

Plus, tweeted mid-process: *"I've found the bottle neck for this stuff can be video rendering time, so I've asked it to make a bunch of renderings at lowres."*

## What we adopted (see PLAYBOOK §11)
| Learning | Where it landed |
|---|---|
| Composable JSON artifacts (edit data, not code) | `templates/cuts.example.json` + `lib_reel.build_segments` |
| Word-level transcription of raw footage + fixes layer | `templates/transcribe_footage.py` + `transcript-fixes.example.json` |
| Incremental segment cache ("new work only") | `lib_reel.cut_segment` (content-hash keyed) |
| Proxy-first (render time is the bottleneck) + divergent previews | `REEL_PROXY=1` in `lib_reel`; rule added to PLAYBOOK §2 Step 5 |
| HTML deck/site → animate, don't just screenshot | note in PLAYBOOK §11 (build on the existing real-screenshots rule) |
| Subagents for ambitious multi-cut work | PLAYBOOK §11 |

Already had before this: word-level VO timing (`vo_words.json`), the inline fixes dict, the Remotion migration plan (§10 Phase 2), and "cutplan-as-JSON" (§7). Thariq validated the direction and turned the proxy + cache ideas from roadmap into shipped code.
