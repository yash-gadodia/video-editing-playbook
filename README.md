# The Video Editing Playbook 🎬

How a small DTC brand ([The Bon Pet](https://thebonpet.com), a fresh pet food company in Singapore) produces short-form video (IG Reels / TikTok) **mostly autonomously with an AI coding agent** (Claude Code) driving ffmpeg, Pillow, Whisper, ElevenLabs, and Remotion.

This is the distilled version of 30+ real videos of trial and error: the pipeline, the hard rules that caused the most pain, the viral content formula we reverse-engineered from reference creators, and the research on what actually grows an account.

The north star: **a postable-quality video out of ONE prompt.** Every rule here exists because skipping it cost us a re-render.

## Contents

| Doc | What it covers |
|---|---|
| [PLAYBOOK.md](PLAYBOOK.md) | The end-to-end production framework: formats, pipeline recipe, hard rules, QA gate, tooling, and the quality-upgrade roadmap |
| [VIRAL-FORMULA.md](VIRAL-FORMULA.md) | The 5-beat content formula synthesized from frame-by-frame study of 9 reference reels |
| [RESEARCH-instagram-growth.md](RESEARCH-instagram-growth.md) | Adversarially-verified deep research: what kinds of videos grow an account (and which "best practices" are folklore) |

## Why an AI agent can edit video (and where it can't)

The core insight the whole playbook is built around: **the agent has no ears and judges from still frames, not motion.** Lip-sync, audio clicks, jitter, and pacing "feel" are invisible to it. So the pipeline is designed to either (a) avoid ever needing those judgments, or (b) convert them into deterministic checks a script can run (coverage gaps, frozen frames, chopped words, loudness). Everything that can't be checked deterministically gets flagged "please verify by playback" instead of claimed as fixed.

Get that division of labour right and the agent handles scripting, curation, captioning, rendering, and QA. Get it wrong and you ship a video with a 1.1s frozen grinder at second 20 (we did).

## License

MIT. Take it, adapt it, ship reels.
