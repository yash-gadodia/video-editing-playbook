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
3. `[FIELD]` **Start the cut ~0.15s BEFORE the first word, never on its timestamp.** A word's acoustic onset precedes its labelled start, so an in-point set to `word.start` puts your 30ms audio fade-in directly on the opening consonant and deletes it. On one interview cut this silently removed the first word of four separate beats ("For", "The", "And" and the brand name) and every frame check passed. Back the in-point off by ~0.15s after confirming the previous word ends before that, drop the fade-in to ~0.015s, and leave caption times anchored to the true word timestamps so they still land correctly. The only thing that catches it is re-transcribing the master and diffing (§12.9) - which is the argument for making that diff mandatory rather than optional.
3c. `[FIELD]` **End the cut well AFTER the last word's END label, and know that the zero-delete diff will not save you here.** Word-END labels undershoot long trailing syllables the same way start labels lead the attack: "Pawrawrdise." was labelled ending 9.30, an out-point at 9.36 audibly chopped the "-dise", and the §12.9 master diff still passed at zero deletes - the decoder reconstructs a truncated word from context, so the gate that catches clipped heads is structurally blind to clipped tails. The founder's ear was the only thing that caught it. Extend the out-point toward the NEXT word's start (9.66 against a next-word start of 9.78 fixed it), budget ~0.3s of tail on any beat ending on a long or stressed word, and verify by isolated decode of that beat off the finished master rather than by the full-take diff.
3b. `[CRAFT]` J-cuts and L-cuts for VO flow: let the next line's audio start before the video cuts (J), or the video move on while the line finishes (L). Hard-cutting both together every time reads amateur.
4. `[CRAFT]` Audio-first editing: place cuts on audio peaks/beats, not arbitrary frames. Extract the waveform, snap cuts to it.
5. `[CRAFT]` Punch-in (5-10% scale jump) instead of a new angle to break up a single take; on the beat.
6. `[OBSERVED]` Face returns to camera for the ONE line that matters most ("this is the part that really matters"). Emphasis = presence, not volume.

## 4. Captions & graphics
1. `[OBSERVED]` Caption pops of 2-5 words, replaced on nearly every phrase - never full sentences (gabrieljudah). Bold, white, drop shadow, centered ~65-70% height.
2. `[OBSERVED]` Story format: 2-line sentence-case captions, one per shot (kaiandjia photo-dump).
3. `[OBSERVED]` Numbered step stickers ("02 CONNECT..." white sticker, colored badge, slight rotation) persist through each step of a how-to.
4. `[OBSERVED]` Live counter/progress-bar overlay animating during talking-head beats (credits bar 38→81→100) gives the eye a moving target. Analogues for a DTC food brand: orders shipped, kg cooked, reviews count.
5. `[OBSERVED]` Every enumerated word gets its own visual: VO says "2nd, 3rd, 4th draft" → screen shows drafts 2, 3, 4.
6. `[CRAFT]` Kinetic typography synced to VO is the current standard; animate titles and CTAs, leave body captions simple.
7. `[CRAFT]` ~85% watch muted: the video must work with sound OFF. Captions everywhere, visual proof over spoken claims.
8. `[FIELD]` **Screenshot web proof at a MOBILE viewport, never desktop.** A desktop-width capture dropped into a 1080x1920 frame is an unreadable postage stamp. Shoot the page at ~430px CSS width (device scale 3) so it reflows tall, then crop a section: it fills the frame edge to edge with type you can actually read. This is the difference between a proof beat that works and one that is decoration.
9. `[FIELD]` **Full-frame proof cutaways should be L-cuts.** Land the cutaway exactly on the words that describe it and let the speaker's audio run underneath unbroken. It reads as evidence appearing mid-sentence rather than as a slideshow interrupting the video. Two cutaways of ~2s each inside a 23s cut was the right dose.
10. `[FIELD]` Sample the screenshot's own corner pixel for the card background colour. A near-white page crop on a brand-cream card leaves a visible rectangular seam that reads as sloppy compositing.
11. `[FIELD]` **Clamp each subtitle's hide time to the next subtitle's show time.** Adjacent caption pills with independent fade-in/out windows will render on top of each other for a few frames. Mine did, and only a frame contact sheet caught it.
12. Safe zones (house rule, kept): nothing in top ~18% of frame; overlays never block faces.
13. `[FIELD]` **Chunk captions on sentence and cut boundaries, not on word count.** A pure N-words-per-pill chunker produced `quite good. I'm` and `here. She's a` - two half-sentences from either side of a full stop, which reads as a transcription bug rather than as a caption. Break after terminal punctuation, break whenever the underlying cut changes, and capitalise the first word of any pill that opens a new cut, because to the viewer a new cut is a new sentence. Word count is the cap, not the rule.
13b. `[FIELD]` **A partner's website photos are evidence of the present, never of the past.** Three product shots scraped off a collab partner's site got laid under their founder saying "there was nothing that actually fit" and "the first one was actually weird". A brand site only ever shows the *finished* garment, shot well, on a happy customer's dog - the exact opposite of the failure the line describes - so the picture quietly contradicted the words. The founder spotted it on first watch. When a beat is about an early failure, a prototype or a before state, the only correct asset is the actual artifact, and the only reliable source is the founder: asked directly, he sent the real prototypes in minutes. Scraping the site is the lazy default and it survives right up until the person who lived the story watches the cut.

13. `[FIELD]` **When a speaker names a specific concrete thing, show that thing.** "The dog keeps jumping on me" and "a very big doberman or something" are both instructions from the subject about what to put on screen. Go and get it: own footage first, then the archive, then a licensed real photo from the web cut out with rembg. Skipping the visual because you do not happen to own it is the lazy default, and the specificity is exactly what makes the line land.
14. `[FIELD]` **Composite cutouts UNDER the caption layer.** A photo cutout dropped on top of everything covers its own subtitle and reads as a sticker pasted over the video. Render it first, let the caption pill sit on top of its legs, and the same asset reads as an object standing *in* the scene. One line of ordering, entirely different perception.
15. `[FIELD]` **Give a web-sourced cutout a brand-coloured outline.** A bare rembg cutout on busy footage reads as a bad composite; a 9px cream stroke reads as a deliberate sticker gag. The outline is what tells the viewer the mismatch is the joke.
16. `[FIELD]` **Pick the licence before you pick the photo.** For anything landing on a commercial account, Pexels / Unsplash / Pixabay beat Wikimedia Commons: most Commons photos of a given subject are CC BY-SA, and share-alike on a derivative work you are publishing commercially is a question you do not want to be answering. The free-stock licences are commercial-use with no attribution required. Still real photographs, never AI - a generated prop undoes the credibility the rest of the edit is buying.
17. `[FIELD]` **A gag tag needs a home that is not a face.** `#NOTSPONSORED` slapped top-right landed squarely on someone's hair. Below the subtitle, rotated a few degrees, it reads as a cheeky footnote to the line above it - which is funnier anyway, because it is annotating the claim.

18. `[FIELD]` **A caption chunk must never span a cut.** Chunking word timestamps by "N words or a gap of X" will happily glue the last word of one segment to the first word of the next, and the resulting pill sits on screen showing text from a different moment. It is guaranteed the moment you reorder segments out of source order. Tag every word with the segment it came from and force a chunk break when that changes. Capitalise the segment-initial chunk too, since cuts routinely start mid-sentence.
19. `[FIELD]` **An emoji can render perfectly and still be invisible.** Checking that the glyph produced a non-empty bounding box proves it exists, not that anyone can see it. A spiral-calendar glyph passed that check at full size and read as *nothing* against dark footage, because it is mostly grey. Choose emoji for contrast against the actual background they will sit on, and confirm on a frame, not in the asset.

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
8. `[FIELD]` **Measure the diegetic track before you promise ASMR, because a room can have none.** Rule 7 says keep the natural sound - it assumes there IS some. Split the band and check: on expo footage the >3kHz region where lapping and crunching live sat at **-44.6dB against a -20.2dB full-band mean, 24dB down**, while <800Hz matched the full mean almost exactly. That is a convention hall, not a cat eating. Lifting the top end to "recover" it surfaces crowd sibilance and hiss, nothing else. Two consequences: never label a cut ASMR before running that measurement, and real eating ASMR needs a close mic in a quiet room, which is a re-shoot and not an edit.
   - **Never `dynaudnorm` room noise.** It hunts for signal in the quiet parts and finds only crowd, so it pumps the hall up to fill every gap - the exact opposite of what you wanted. Highpass hard (150Hz), set a fixed low gain, and let a bed carry the piece.
   - When the diegetic track is pure noise, invert rule 5's balance: bed forward (~0.34), room dropped to texture (measured -38.5dB from -20.2dB). It works standalone, and trending audio can still go on in-app by pulling original audio down there rather than stacking a second bed.
9. `[FIELD]` **Read every caption back as a stranger would, hunting for the reference you did not intend.** "two cats, one cup" shipped past me onto a pet food cut before the founder caught what it echoes. Wordplay that scans well in a build script is exactly the kind that has a second reading, and food brands are unusually exposed because so many shock references are about eating. The check costs seconds and the failure mode is a brand-safety incident, so run it on every line: say it aloud, and if any well-known phrase shares its shape, rewrite rather than tune. Avoid the whole construction, not just the wording - "one cup" in any arrangement lands in the same place.

## 6. Structure (the retention skeleton)
1. `[OBSERVED]` The AI-demo/how-to skeleton (gabrieljudah, 122s): promise → free/easy → "but here's the catch" → most-people's-mistake → the opposite → receipts ("that video went viral", counts on screen) → numbered steps → quotable aphorism → comment-keyword CTA.
2. `[OBSERVED]` The story skeleton (kaiandjia, 5.8M): chronological adversity arc in captions over real archival footage; the business is the PAYOFF of the personal story, never the topic.
2b. `[FIELD]` **Lay every cut against hook / premise / conflict / resolution, and check the PREMISE act specifically - it is the one that silently goes missing.** A finished cut reviewed by our agency partner had a hook, an obvious conflict and a long resolution, and still needed work, because nothing on screen ever established *who the subject was*. The load-bearing fact - that she was 15 - lived only in the post caption. Hook and conflict are the fun acts so they get built by instinct; premise is boring exposition, so it gets deferred to the caption, where rule 1.8 says almost nobody reaches it. The test: mute the video, watch the first five seconds, and ask whether a stranger knows who this is and what is at stake. If the answer only exists in the caption, it is not in the video. Fix is cheap - a pinned context banner (rule 1.4) held over the opening act and dropped the instant the conflict starts. Style it differently from any other persistent pill you use (ours: orange banner vs teal interview prompts) so it reads as a standing label rather than as dialogue.
2c. `[CRAFT]` Watch act 3 for bloat once the acts are named. Ours came out 25s of a 36s cut. Back-heavy is not automatically wrong - the long tail there was competence evidence, without which the piece reads as pity - but you should be choosing it, not discovering it.
3. `[CRAFT]` Mini open-loops in the body ("I'll come back to this"); attention reset every 20-30s (twist, cutaway, sound spike).
4. `[CRAFT]` Loop-back endings (last shot flows into the first) inflate completion via replays.
5. `[OBSERVED]` Receipts beat: show real numbers on screen (view counts, revenue, order counts) during the fastest-cut section.

## 6b. What actually made the difference (measured, not felt)

1. `[OBSERVED]` **Shares separate a hit from a flop, and nothing else comes close.** Across one account's recent output, the single reel that reached ~3x follower count took 18 shares and 227 interactions; everything the brand produced itself took 0 to 2 shares and 3 to 16 interactions. Shares are a confirmed ranking signal, so this is a mechanism and not a mood. Before rendering, ask the concrete question: who forwards this to whom, and what does sending it say about the sender? If there is no answer, the edit will not save it.
2. `[OBSERVED]` **Carousels are the save format; reels are the reach format.** A static carousel with under 1,000 views collected 6 shares and 5 saves, more than any reel on the account. Put reference material (numbers, comparisons, receipts) in carousels and motion-dependent storytelling in reels, rather than forcing everything into video.
3. `[OBSERVED]` **Reach does not convert to follows on its own.** A reel at ~3x follower count produced one follow. If follower growth is the goal, the ask has to be built into the piece; volume alone does not do it.
4. `[FIELD]` **Pull the numbers from the platform's content table, not the public grid.** Logged-out grid counts were 35% low against the same post's logged-in figure, and the grid hides shares, saves, watch time and average play time entirely. The deeper columns are where the lesson is.

5. `[FIELD]` **Shares, saves and follows are three different behaviours with three different triggers. Decide which one the piece is for BEFORE the first cut.** Shares come from identity signalling (the viewer forwards it because it says something about them, "this is my cat exactly"), so the subject has to be recognisably *theirs*, not yours. Saves come from utility, which is why reference material belongs in a carousel and not a reel. Follows come from repeat profile visits, so a one-off hit converts almost nobody: episodic, numbered content is the only lever we have evidence for. A piece aimed at all three lands none.
6. `[OBSERVED]` **Borrowed audience beats better production, by an order of magnitude.** The one post on our account that reached ~3x follower count was a collaboration with an established creator, published as a collab post, using their footage and their caption. Nothing the brand produced in-house came close on any engagement metric. If reach is the goal, the lever is whose audience you are borrowing, not how good the edit is.
7. `[FIELD]` **When the research contradicts your own numbers, your numbers win.** A creator-format study concluded that founder talking-head content does not work. Our own account says otherwise: a founder piece answering public criticism did ~6x median. The distinction the study missed is register, not format. Founder *announcing* fails; founder *confessing or being challenged* travels.

## 7. UGC-sourced edits (compilations, testimonial reels)
1. `[FIELD]` **QA every chosen clip's baked-in text for creator promo/referral codes AND third-party brand handles BEFORE building.** Customer story reposts often carry the creator's personal discount code, or a tag of another brand they feed alongside yours (e.g. a kibble-mix combo), baked into the frame. Either one can land on exactly the wrong beat of your script. Cropping rarely hides it cleanly - replace the clip instead.
2. `[FIELD]` Visible usernames/story stickers in UGC are receipts, not clutter - keep them. They ARE the authenticity. Place your overlays around them.
3. `[FIELD]` Caption y-position is per-clip, not global. A y that clears one clip's subject sits on the next clip's face. Split a caption into windows with different y per segment when the subject moves (and re-check every window against faces - a top-of-frame default is not an answer).
4. `[FIELD]` Check your display font's glyph coverage before shipping stickers - symbol glyphs (e.g. ★) silently render as nothing in some display fonts. Spell it out ("4.8/5") or render the symbol as an emoji layer.
5. `[FIELD]` Survey footage by contact sheet (1 mid-frame thumb per clip, grid, indexed), shortlist, then verify motion with 3-frame strips per candidate. Never pick from filenames.
6. `[FIELD]` **Audit coverage against the transcript BEFORE you write the cut, not at render time.** Ask of every strong line: is the thing being described actually on camera? Our best line was a customer saying her ten-year-old rescue "doesn't eat anything random" - and that cat was never once filmed eating. Only her two housemates were. The trap is that a cat-eating shot under a "she" line looks fine and is quietly false. The fix is structural: land eating shots on the lines about the animals who are eating, and give the named one her own shots. You cannot discover this while placing clips; by then the script is already committed.
7. `[FIELD]` **A caption is a claim, and it inherits the burden of proof.** "They finished the lot" got written because it scanned well, not because any frame showed it. What the speaker had actually said - "they are still eating now" - was both defensible and better. Whenever a caption asserts something the footage does not show, the transcript almost always already contains a truer line; use that one.
8. `[FIELD]` **A trade-show booth is a free interview studio, and the constraint is consent, not craft.** One morning at a stand produced a mic'd interview, close-up b-roll and a finished collab cut inside an hour, because the subjects were already there, already customers, and already delighted. Clip a lav on, ask three questions, and shoot the b-roll BEFORE the interview so the cutaways exist when you need them.

9. `[FIELD]` **An on-screen counter is a claim, and montage footage almost never supports one.** A "REJECTED x1..x4" tally over four walk-past shots was built, looked great, and was wrong: one of the four subjects is standing AT the tray three seconds later, so the badge asserted the opposite of what the same clip showed. Counters feel like decoration because they are graphics, but they are assertions with a per-item burden of proof, and you incur it four times instead of once. The fix that improved the cut: delete the tally and let the subject's own line ("that's three in a row") carry the number. Her claim, from her mouth, is both better evidence and better television than your badge. Before rendering any counter, tally, score or streak, verify EVERY item it counts - and if the subject already said the number out loud, use that instead.

10. `[FIELD]` **A word that decodes cleanly in isolation can decode differently off the finished mix, and disagreement across CONTEXTS counts the same as disagreement across temperatures.** Rule 9.8 sweeps temperature on one audio source; this is the sibling failure. A reply came back "No, thanks." three times from the cleaned raw take and "Okay." twice from the same window re-decoded off the delivered render. Both were confident. There is no tiebreak available, so it does not ship as attributed speech. Note this is only findable BECAUSE §12.9 makes you re-transcribe the master - the diff is not just checking that words survived the cut, it is a second independent decode of every line you are about to attribute to a real person. Cheapest resolution when it matters: ask whoever was in the room. Second cheapest: cut the caption and let the beat play silent, which here was better anyway, because a question nobody answers is the entire point of the shot.

11. `[FIELD]` **When the camera drifts off the action, move the PICTURE, never the words.** The moment a sale closed, the lens was pointed at someone's dog and the floor. The temptation is to caption the audio anyway and let a dog shot stand in for a transaction. Two honest options exist: cut a picture-only cutaway from elsewhere in the SAME continuous interaction and let the real audio run underneath (a normal L-cut, rule 4.9), or drop the claim and end the arc on something you can prove. Taking the second option cost a cha-ching and a "SOLD" card, and the cut got better - the payoff became the subject saying she was less nervous than at her first event, which is the actual story. A reel does not need the transaction; it needs the change in the person.

12. `[FIELD]` **Build the opening beat by asking "what is frame one", not "what happened first".** A cut opened on the chronological start - the subject walking up to a stranger asking "does anyone want to try?" - and the founder's entire review was "why first frame liddat". It was an establishing shot OF a greeting, which is rule 1.5's forbidden pair twice over, and the subject was small enough that the frame was dead at thumbnail size. The trap is that chronological order feels like structure, so the weakest available image gets the most valuable slot in the video by default. Fix: pick the best FACE-to-camera shot you own for frame one (rule 14.2), open on it mid-thought with no context, and let the next two beats supply the context. Opening on "it's okay, it's a life lesson" before the viewer knows what went wrong is an open loop; opening on the greeting that caused it is a slideshow. Same footage, same length, entirely different first second.

13. `[FIELD]` **Identify who is who by wardrobe BEFORE writing a line of the edit, whenever two subjects share a uniform.** Two part-timers in identical branded aprons: the one facing camera during the cut's best line was not the subject, who had her back turned three feet away. Everything downstream inherits this - which shot can carry an attributed quote, which frame can be the cover, and whether the post caption's "she said" is true. Pick a durable discriminator (tee colour, not hair or position, both of which change shot to shot), write it into the build notes, and re-check it at every beat where someone is credited with speech.

## 8. What we explicitly do NOT import (quarantined folklore)
Our adversarial research (200+ agents, ~190 claims, 6 survivors) killed the marketing-blog versions of: trending-audio reach multipliers, micro-influencer superiority, optimal posting cadence, format-type preference stats, "67% more trusted" UGC numbers. The verified fundamentals remain: **watch time, completion, replays, shares** are the ranking signals; read first-party retention data, not listicles.

## 9. Source prep (do this before a single cut)

1. `[FIELD]` **Check the source colour space first.** `ffprobe -show_entries stream=color_transfer,color_primaries`. If it reports `arib-std-b67` (HLG) or `smpte2084` (PQ), the file is HDR and feeding it straight into ffmpeg will wreck the colour. Modern phones record HDR by default, so this is now the common case, not the exotic one.
2. `[FIELD]` **Two ways to get HDR wrong, both shipped by me in one session.** (a) Decode it naively: ffmpeg ignores the tags, reads the HLG curve as if it were gamma and BT.2020 values as if BT.709, and you get a flat, washed-out, undersaturated image. It looks "fine but dull", which is exactly why it slips through review. (b) Hand-roll an HLG to BT.709 3D LUT: the classic bugs are applying the HLG OOTF at gamma 1.2 (that is the *1000-nit* system gamma) on top of the display gamma, which double-counts system gamma, plus a full BT.2020 to BT.709 matrix on content that is effectively near-709 gamut. Warm tungsten skin and walls go orange. The review verdict on that render: "why so red? looks weird like a bad filter".
3. `[FIELD]` **The fix: let the OS tone map, do not reimplement it.** On macOS, pre-transcode to an SDR BT.709 master with AVFoundation, then run the entire ffmpeg pipeline on that master. `templates/tosdr.swift` does it in about 20 seconds for 38s of 4K, keeps audio and exact timing, and bakes in the rotation so there is no display-matrix side data to handle downstream. The usual `zscale=t=linear,tonemap,zscale=p=bt709` recipe is unavailable on ffmpeg builds compiled without libzimg, and that absence is precisely what tempts you into the hand-rolled LUT. Do not take the bait.
4. `[FIELD]` **Get a ground-truth reference frame before judging any grade.** `AVAssetImageGenerator` returns a system-tone-mapped still, the exact thing the OS video player shows. Render your version beside it and LOOK. Do not trust "mine looks richer than the raw decode" as evidence of correctness; richer was the failure mode. `templates/ref_frame.swift`.
5. `[FIELD]` **A numeric fit that bottoms out at the edge of your parameter grid is telling you the approach is wrong, not that the parameters need tuning.** I swept OOTF gamma, primaries matrix, exposure and desaturation against the reference; the best fit still had ~27/255 mean absolute error and kept pushing toward the grid boundary. That was the signal to stop tuning and delegate the transform.
6. `[CRAFT]` Transcribe the raw take at word level before planning cuts. The transcript, not the waveform, is the edit decision list for anything with speech.
7. `[FIELD]` **Whisper hallucinates a repeated-word loop over quiet stretches, with confident timestamps.** A 24s no-speech gap in a noisy hall came back as one segment reading "I thought I was walking home home home home..." about sixty times, spanning 65.8 to 89.1s. Nothing marks it as low confidence, and it silently swallowed the best exchange in the take. Detection: any segment whose duration is huge relative to its word count, or with an obviously repeated token. Fix: re-transcribe that window on its own and add the offset back.
8. `[FIELD]` **When a word matters, decode it three ways before you burn it into a caption.** A line came back as "studying dreddy cooked", "studying generally cooked", "saying ready cooked" and "studying Jaday cooked" across passes - consistently confident, consistently wrong. What disambiguates: isolate the snippet and clean it (`highpass=f=90,loudnorm=I=-16`), slow it (`atempo=0.7`), and decode at two temperatures. Passes disagreeing IS the signal that the word is unreliable. Anything still unresolved gets flagged to whoever was in the room rather than shipped as a confident quote - subtitles are attributed speech, so a mis-heard verb is a factual error, not a typo.
9. `[FIELD]` **A transcript reading exactly `"Thank you."` usually means the track is digitally silent, not that someone said thank you.** Two takes from a multi-take shoot came back with that single string; slowing them down and re-decoding returned the same string, which is the tell that there is nothing to decode. `ffmpeg -i take.mov -af volumedetect -f null -` showed **-91 dB mean AND max** - the wireless mic was never live for those takes. Run volumedetect across every clip before planning the edit, because a dead mic on the hero take changes which take is the hero. Note volumedetect writes to **stderr**, so `-v error` silently swallows the numbers.
10. `[FIELD]` **Clamping a caption's time to the segment boundary does not remove its words.** Trimming the tail off a segment (to cut a flub, a break in character, a repeated line) leaves any caption chunk that straddled the cut still printing the words that are no longer spoken - the pill hides on schedule but shows the wrong text until it does. Filter words to `src_in <= w.start and w.end <= src_out` **before** chunking, not after. This is the sibling of the overlap bug in section 9 rule 11, and like it, it is invisible in the render log and only shows up on a frame contact sheet.
10b. `[FIELD]` **A clean word-level timestamp in a full-take pass is not evidence the word is audible.** The decoder has a language model and it will happily invent a plausible leading word from context, complete with a tidy 0.4s span. One take labelled `Nick, 63.28-63.68` before "ask me some questions" - obviously right, he was addressing his co-founder, and the shot showed it. Decoded on its own at two temperatures, that same window came back as *Icelandic gibberish*, which is what this model does with sub-second noise. The isolated decode is the honest one, because it is the only pass with no neighbouring words to lean on. Isolate any word you are about to caption that sits at the very start or end of a segment, and expect the full-take pass to be the optimistic one.

10c. `[FIELD]` **Survey frames at every segment's IN and OUT point, not on a uniform grid over the take.** A 4-second contact sheet of a 110s interview showed the subject in frame at 72s and again at 84s. What it did not show was that the camera swings onto the ceiling and a neighbouring stand from 75.9 to 82.5 - so a beat cut at 72.6-79.3 put the payoff of the entire hook over two seconds of motion-blurred clothing rail, and the render's own contact sheet was the first place it appeared. A uniform survey answers "what is in this take"; it does not answer "what is in *this cut*". Sample the actual in/out of every segment before committing the cut list.

10d. `[FIELD]` **When the picture under your best line is unusable, look for the restatement before you look for a cutaway.** The instinct is to L-cut something over it. Cheaper and better: people repeat themselves. The unusable "and we have to earn it back" was said again ten seconds later, in frame, with a comic button attached ("our customers are supporting us... but still, it's still expensive"). Search the transcript for the same idea before you start plumbing a cross-clip insert.

11. `[FIELD]` **Cloud-synced archives lie about what you actually have.** Files in an iCloud/Drive-backed folder list real byte sizes while holding no local data; the tell is `st_blocks == 0` (or `du -sh` on the folder returning 0B). Materialising is slow enough to wreck a session's plan - roughly 25 of 296 clips in several minutes even with 8-way parallelism. Start any archive pull in the background at the very top of the session, and never design a beat around footage you have not already got on local disk. While you are there: many phone-library "clips" are Live Photo stubs of about 5 frames, so ffprobe the duration before picking one.

## 10. Interview & collab formats (the highest-leverage shape we have found)

1. `[OBSERVED]` **Stacked split-screen interview.** Guest fills the top pane, host the bottom, both talking heads, no empty frame. The listener's face is doing real work: it gives the scroller a reaction shot and a reason to stay. Observed on a collab interview of our founder by a pet-media account; it is the same shape used across the interview-clip economy.
2. `[OBSERVED]` **Yellow word-by-word captions at the seam between the two panes.** High-contrast yellow reads on skin, walls and clothing alike, which is why it is the default in high-retention interview clips. Worth A/B testing against a brand-coloured caption, because brand colours are chosen to look correct, not to survive a 4-inch screen at arm's length.
3. `[FIELD]` **One long interview is a series machine, not one video.** A 7-minute founder interview cut at question boundaries yielded 10 self-contained clips (0:13 to 1:14 each). Each answer already opens with its own question, which IS the hook. Film once, ship for weeks.
4. `[FIELD]` **Question design decides whether the answers are usable.** The questions that produced shippable clips all forced a confession or a contradiction: "if you started over, what would you change", "what was the biggest problem", "how did you get your first 100 customers". The ones that produced flat answers were positional ("how do you think about competitors"). Write questions that can only be answered with a loss, a number or an admission, per rule 1.2.
5. `[FIELD]` **Answers that break the expected script travel furthest.** The strongest lines in our own interview were the ones that refused the premise: "I don't think the business has actually taken off, we're just getting started", and naming the biggest mistake as something the founder chose to do. Prompt for those explicitly, they rarely arrive unprompted.
6. `[CRAFT]` **Plant an open loop inside the interview.** Two separate answers teased an upcoming transparency drop ("stay tuned, we are publishing every single dollar"). That converts a one-off interview into an on-ramp for the next launch.
7. `[FIELD]` **Always publish partner content as a collab post**, not a repost. It lands on both grids and both follower feeds. In our own data, collab posts run 1.5 to 2.6x median while brand-owned announcements run at or below it.
8. `[FIELD]` **Ship the raw interview to the partner as frame-accurate clips plus a word-level transcript and a shotlist.** They edit faster, they credit accurately, and you keep an identical set to cut your own versions from later.

9. `[FIELD]` **If the interviewer has no mic, cut their audio entirely and put the question on screen as a written prompt.** Holding a small pill at the top of frame for the whole answer, instead of playing an inaudible question, removed 10 seconds of dead and unusable audio from a 52s cut - a 20% runtime saving made entirely of material nobody could hear anyway. It also reads *better*: the prompt is a persistent title the viewer can re-read at any point, where a spoken question is gone the instant it is said. Bonus, and the reason it is a rule rather than a trick: you stop having to guess what the muffled question was, because you are now writing it rather than transcribing it. Hold the same prompt unbroken across a cutaway so the question survives the b-roll.
10. `[FIELD]` **Answers are short; questions are the skeleton.** Once questions are on-screen prompts, phrase them shorter and more casual than they were actually asked ("funniest customer so far?", "still studying?"). They are now design elements, not a transcript.

11. `[FIELD]` **Cut the interview into a story arc, not the order it was asked in.** A raw Q&A is sequenced by whatever the interviewer thought of next, which is almost never the best running order. Reordering one 115s booth interview into hook-on-the-numbers -> product tease -> the human pay-off -> forward look turned a rambling answer set into a 24s story, using nothing but the subject's own sentences. The interview is raw material; the arc is the edit. Corollary: because the viewer never sees the questions, you are free to move any answer anywhere.
11b. `[FIELD]` **An aside moved to the end becomes the resolution.** Rule 11 says reorder freely; this is the highest-value single move inside it. A founder muttered "as [the part-timer] said, it's part of the process" at 34s of a 276s take, in the middle of a run of rejections, where it read as a throwaway. Placed last it became the whole point of the piece - the boss consoling himself with his junior's advice. Nothing about the words changed. When a cut has a hook and a conflict but no ending, do not go looking for new material; scan the transcript for the line that is *reflective rather than descriptive* and move it to the back.

11c. `[FIELD]` **Whether to drop the interviewer's audio is a measurement, not an assumption.** Rule 9 assumes the person behind the camera is off-mic. Check before you build around it: on one booth interview the interviewer ran **-14.5 to -21.5 dB against the subject's -17 to -20 dB**, because he was holding the phone and the subject was on a handheld pointed at his own chest. Keeping both voices turned a Q&A into a two-hander, and the back-and-forth ("can you say properly please?") was the funniest thing in the cut. Same rig, same room, opposite call from the day before - so measure per take, not per format.

11d. `[FIELD]` **A host's series-launch intro slots AFTER the subject's hook, and should end on the subject's name.** Shooting a separate to-camera clip ("here's why we're doing this series") tempts you to open with it, which is rule 1.5's forbidden greeting-open. Splice it as the premise act instead: subject's confession hook first, then the host beat, and cut the host's beat so its last line names the subject ("this will be our first brand, Pawrawrdise") - the subject's own self-intro then answers it and the seam disappears. Put the host's series-name line and the follow-ask at the END, next to the card: the follow-ask converts on episodic content, and a name said aloud as a pun ("suppawt, support local") can run under a caption showing the spelling - audio carries the pronunciation, the pill carries the brand.

12. `[FIELD]` **Cut every scrap of dead air EXCEPT the beat before a punchline.** The speech-density rule is right up until it eats the setup. A one-word answer ("how many events have you done?" / "Countless.") ran 0.87s on its own and read as a glitch, especially sandwiched between two b-roll shots - the speaker's face flashed up and vanished. Restoring the thinking pause before it and a hold after, 1.57s total, turned the same words into the funniest beat in the cut. Air that carries a reaction is content; air that carries nothing is filler. Land the sound effect on the spoken word rather than on the cut, and hold the on-screen question through the pause so the viewer is waiting with the speaker.

## 11. Showing a real document (redaction is a format, not a chore)

1. `[CRAFT]` **The redaction IS the hook.** A blurred real document signals "this exists and I am choosing what to withhold" in a way a clean designed graphic cannot fake. Withholding reads as more honest than showing nothing, and more credible than a mockup. The reaction to our own build of this was the strongest we have had.
2. `[FIELD]` **Redact default-deny: blur the whole frame, then restore only the regions you have explicitly cleared.** The intuitive way round (list the regions to blur) leaks. A first pass over ten spreadsheet tabs missed the summary rows, because they sat outside every rectangle we had thought to name.
3. `[CRAFT]` **Keep the labels sharp and kill the values.** Row and column headings readable, figures blurred. The viewer sees *what* is tracked without the numbers, and the surviving structure is exactly what makes it read as genuine rather than staged.
4. `[CRAFT]` **Number the versions.** A montage of near-identical screenshots is boring. The same montage labelled V1 through V7, each with one line on what that version tried, becomes a progress narrative with a destination. The label carries the meaning, so individual cells never need to be legible.
5. `[FIELD]` **Read the margins of every screenshot before it ships.** Working documents carry things the story does not need: third-party ad spend, vendor and contractor names, competitor names. One tab in our own set had all three parked in unused columns. Blur by region, not by data type.
6. `[CRAFT]` **End on the one thing you ARE publishing.** After a run of redactions, the single unblurred artefact is the emotional pay-off.

7. `[FIELD]` **A payment QR caught in your own footage has to be covered before the video ships.** Event signage, counter cards and table talkers carry live payment codes, and a viewer can scan one straight off a paused frame from their sofa, with no order and nobody at the till to catch it. Treat any scannable code on screen as a live endpoint, not as decoration, and check for it on every frame where the sign is legible.
8. `[FIELD]` **Replace the covered region with content; do not smear it.** A `boxblur` over a QR rendered as a lurid pink rectangle (the code's own colour smearing out), read unmistakably as a censorship bar, and still leaked the "scan to pay" strip below it because the box was sized to the code and not to the block. An opaque brand-coloured panel carrying real information in the same footprint - the opening times, in our case - reads as part of the printed sign instead, and the dead space starts doing work. This is the inverse of rule 1: withholding is the hook when the *document* is the story, but when you are hiding one incidental element inside an otherwise fully-shown artefact, visible redaction just looks like damage.
9. `[FIELD]` **Size any fixed cover against the object's DRIFT, not against one frame.** Handheld footage of a held-up card moves throughout the shot. Sample frames across the whole window first, then size the panel to sit inside the object's own edges at every one of them - ours went 684px wide inside a card spanning 897px. Get this wrong and the thing you were hiding reappears at one end of the shot, which a single-frame check will never show you. While measuring, note where the object stops being readable at all: ours survived 0.8-3.5s of a 5.7s clip and the camera panned off it after that, which set the beat length.
10. `[FIELD]` **Punch into a real sign from the full-resolution master, never from the delivery render.** Cropping a 1426x2534 region out of a 2160x3840 tone-mapped master and scaling it to 1080x1920 is a downscale, so the printed offer lands razor sharp; taking the same crop from the finished 1080-wide cut is a 1.5x upscale of identical content. The legibility of the sign is the whole point of the beat, so spend the pixels where they exist.
11. `[FIELD]` **DECODE every code you find before deciding it is harmless, from the source resolution, upscaled.** An unlabelled white "scan me" card sitting on a booth shelf looked like a follow-us prop and decoded to a live PayNow payment payload. Two traps stack: you cannot know a code's function by looking at it, and the detector's failure is not evidence of illegibility - `cv2.QRCodeDetector` returned nothing on the 1080p delivery frame while a 2-3x cubic upscale of the same crop from the 2160p master decoded instantly. Test at source res, with a sharpen pass, before concluding a code is below legibility. Concrete floor from the same measurement: an instance ~130px wide at delivery decodes; instances under ~50px cannot resolve no matter how a viewer zooms, because the pixels do not exist. Cover the big ones, let the sub-50px background sightings go, and write the threshold into the build notes so the next pass doesn't relitigate every speck.
12. `[FIELD]` **When a live code drifts across a panning shot, replace the shot, not the pixels.** Chasing a card across a pan means keyframed cover windows that teleport with every camera move, and every missed frame is a leak. The audio does not care what the picture shows: an L-cut cutaway from elsewhere in the same take over the untouched voice line removed the entire problem, read better than the original blurry pan, and cost one line of the beat table. A moving cover panel is the last resort, not the default.

## 12. Rendering integrity (the failures that ship silently)

1. `[FIELD]` **Never `zoompan` a static card.** It rounds its crop offset to whole INPUT pixels each frame, so a slow push-in on a still oscillates about a pixel and reads as shake. Supersampling the source 2x halves it but does not remove it (measured: 5 one-pixel reversals across 43 frames). Animate opacity instead: `scale=W:H:flags=lanczos,fps=30,setsar=1,fade=t=in:st=0:d=0.30` over a `-loop 1 -t DUR` still. Alpha cannot quantise position, so shake becomes structurally impossible rather than merely reduced.
2. `[FIELD]` **`zoompan`'s `d=` counts output frames PER INPUT FRAME.** Hand it a looped still and every input frame spawns a full `d=` run, so each card silently becomes minutes long and `-shortest` truncates the timeline to the first one. Feed exactly one image, no loop, and cap with `-frames:v N`.
3. `[FIELD]` **Join segments with the concat FILTER, not the concat demuxer.** The demuxer assumes every input already shares codec parameters and silently mistimes them when they do not. A clip that inherited 44100 Hz from a phone source, joined to segments encoded at 48000 Hz, held its last frame for ~1s at the seam. The filter re-normalises fps, scale, sample rate and channel layout per input, so the whole class of bug disappears.
4. `[FIELD]` **Pin `-ar` and `-ac` on every intermediate encode.** Sample rate is inherited from the source when unset, so segments built at different moments drift apart with no warning. Decide one canonical spec (resolution, fps, pixel format, sample rate, channel layout) and force it on every intermediate.
4b. `[FIELD]` **Keep intermediates in PCM, and force each segment's audio to exactly its video duration.** Rules 4 and 11 pin the spec and catch the drift; this removes the cause. AAC adds encoder priming/padding, so an intermediate's audio ends up marginally longer than its video, and the concat filter pads every segment to whichever stream is longer. A 14-segment join drifted +4 frames with every sample rate already identical and every `-frames:v` already pinned. Encode intermediates `-c:a pcm_s16le` and run the audio through `apad,atrim=0:<dur>` so v and a are equal by construction; encode AAC once, at the end. The frame-count assert catches it either way, but this is what stops it happening.
5. `[CRAFT]` **Assert duration after every join.** Compare the output against the sum of its parts and fail loudly past a small tolerance. The freeze above was sitting in the numbers (10.97s expected, 11.97s actual) long before anyone saw it on screen.
6. `[FIELD]` **Verify motion numerically, never by eye.** For frozen frames, decode at ~10fps and flag runs where consecutive frames differ by near zero. For jitter, cross-correlate consecutive frames: try a shift of -1, 0 and +1 px per pair and check which alignment minimises the difference. All zeros means genuinely static. Edge-threshold tests give false positives on anti-aliased curves, which is how a card that is provably static can still look like it is moving.
7. `[FIELD]` **Display fonts carry no emoji glyphs, and PIL drops them silently** - no tofu box, just nothing where the emoji was. Either omit emoji from rendered cards or draw them from the system colour-emoji font with `embedded_color=True`, which accepts only fixed strike sizes. Emoji in the post caption are unaffected. A grey paw on a dark brand colour reads as a smudge regardless; let the logo carry it.
8. `[CRAFT]` **Auto-fit caption text to a safe width.** A point size that fits one line will overflow the frame on the next. Shrink until it fits, then wrap.
9. `[FIELD]` **Re-transcribe the finished render and diff it against your intended caption list.** It is the cheapest possible proof that no cut clipped a word's head or tail, that every beat you planned actually survived the concat, and that nothing you meant to remove is still audible. Two minutes, and it catches a class of error that watching cannot.
9a. `[FIELD]` **The baked music bed poisons the master re-transcription's word identity, not its word presence.** Once the mix has a bed and SFX under the voices, the re-decode of the finished master returns the same word COUNT in the same places but mangles what the words are ("not sponsored" -> "so awesome", "thank you thank you" -> gibberish), so the diff fills with `replace` opcodes that look alarming and mean nothing. The deletes gate still works - deletes stay structural. But never re-litigate a word's identity from the render decode: the clean-source decodes are the honest ones for WHAT was said, the render decode only proves the words survived the cut. Two agreeing source-side decodes beat any number of render-side disagreements.
9b. `[FIELD]` **Read the DELETE opcodes, not the similarity score.** The diff's two directions are not equally serious. An `insert` (the master has words your caption does not) is speech filler you deliberately tightened out - fine, expected, ignore. A `delete` (your caption has words the master does not) is a caption asserting speech nobody can hear, which is the whole failure mode you ran the diff to find. A `replace` is almost always the transcriber mangling a proper noun; verify it against the brand's own site and move on. On one 48s cut the score read 87.8% and "looked fine" while hiding three real defects; driving them out moved it only to 92.3%, because the percentage is dominated by filler words that never mattered. **Ship at zero deletes, not at a number.**
9c. `[FIELD]` **A 20ms word timestamp is not a duration, it is a warning that two people are talking at once.** The transcriber crushes the tail of the first speaker's word into a near-zero span and starts labelling the second. On one answer "time" was labelled 128.30-128.32 while the interviewer's next question began at 128.35, so **no out-point existed that kept her clause and excluded his**. Cutting on the label ate "full time"; extending 130ms let the spoken question bleed in. Do not micro-adjust - two attempts is the limit, and this is not a timestamp problem. Caption only what is provably on the track and let the on-screen written prompt carry the rest: under a prompt reading "you do this full time?", a curt "No, I'm not doing this." is both honest and a harder confession than the full sentence. Confirm by slow-decoding that beat *out of the finished master* at two temperatures.
10. `[FIELD]` **`sips` only applies EXIF rotation when it resamples.** Converting a phone photo with `-s format png` alone hands back the stored raster - a portrait shot arrives landscape, and asking for a max dimension equal to the existing one is a no-op that silently skips the rotation too. Check `width > height` after conversion and rotate explicitly rather than trusting the tool.

11. `[FIELD]` **Snap every segment to a whole frame, and assert the FRAME COUNT, not the duration.** Pinning `-ar`/`-ac` (rule 4) is necessary and still not sufficient: each segment's video is rounded UP to a frame boundary on encode and the container adds its own audio padding, so an eleven-cut join drifted +0.44s against the caption timeline with every sample rate already identical. A duration assert with any sane tolerance passes that build. Compute each cut as `round(dur*fps)/fps`, join with the concat filter, then compare `ffprobe -count_frames` against the expected total - an integer equality that cannot be fudged.
12. `[FIELD]` **Anchor overlay windows in SOURCE time, never in timeline seconds.** Rule 11 keeps the timeline honest; this keeps the graphics attached to it. Captions get re-derived from word timestamps every build, so they self-heal - hardcoded sticker and SFX positions do not, and they drift by exactly the same amount with nothing to catch them. Express every sticker and SFX window as a timestamp in the original take and push it through the same source→timeline map the captions use, building that map from the MEASURED duration of each encoded segment and mapping interior points proportionally. Then re-cutting any segment slides the graphics along with the words instead of stranding them a third of a second late, and an assert that every window resolved inside a surviving cut catches the ones you trimmed away.
15. `[FIELD]` **Settle orientation ONCE, into a shared raster, before the build starts.** Rule 13 says the two tools disagree; the fix is not to remember which is which at every call site. Pre-pass every phone still into a scratch `upright/` directory - open it, rotate if `width > height`, re-save as a fresh PNG - and point the build there. The re-encode drops the orientation tag entirely, so ffmpeg and PIL agree by construction rather than by vigilance. Doing this lazily cost a shipped end card: the still was composed against the PIL view and rendered from the ffmpeg view, and the partner brand's banner ended up sliced off the left edge.
16. `[FIELD]` **Cover-cropping a 3:4 photo into 9:16 throws away a quarter of the width, and edges are where signage lives.** For a photo whose value is text near a border - a booth banner, a shopfront, a printed sign - fit to width and pad onto a brand colour instead of cropping to fill. The letterbox reads as a deliberate card; the crop reads as a mistake, because it is one.
13. `[FIELD]` **ffmpeg honours EXIF orientation and PIL does not.** The same JPEG previews upright through ffmpeg and composites on its side in PIL, so every preview you generate can look correct while the delivered still is rotated. Run `ImageOps.exif_transpose` on load for anything originating from a phone, and never take an ffmpeg-made preview as proof that a PIL-made composite is right. This is rule 10's trap wearing a different coat: two tools, two answers, same file.
14. `[CRAFT]` **Keep render intermediates off cloud-synced folders.** Hundreds of overlay frames plus a lossless overlay track inside an iCloud/Drive-backed directory invites the file provider to sync or evict a file mid-render; one job died with a bare non-zero exit and no message. Point the scratch directory at local disk and keep only the deliverable in the synced tree - it also ran roughly 40% faster.
15. `[FIELD]` **Eviction hits your SOURCES too, and `ls` will lie to you about it.** Rule 14 treats this as an intermediates problem; it is not. Come back to a build an hour later and the provider may have evicted a source master you already transcoded - `ls -l` still reports the full 92MB because the logical size is metadata, while `du -sh` reports **0B** because no bytes are local. ffmpeg gets a dataless placeholder and dies with a bare exit 196 and no diagnostic, which reads as a code bug and sends you debugging the filter graph. Check `du`, never `ls`, and hydrate with `brctl download` (or `cat file > /dev/null`) before any rebuild. Cheapest insurance: guard the build with a `du`-based eviction check that rehydrates automatically, because a session that renders once fine will fail on the rebuild an hour later.

16. `[FIELD]` **On an overlay-only re-render, prove the audio bit-identical instead of re-running the transcript gate.** A graphics fix (caption spelling, an ident lockup) rebuilt through a deterministic pipeline should not touch a single audio sample. Decode both renders to raw PCM (`ffmpeg -vn -f s16le -` piped to a hash) and compare: a matching hash means the original §12.9 zero-deletes verification carries over wholesale, which is both faster and stronger than a fresh Whisper pass over the baked mix (which rule 9a says mangles word identity anyway). A mismatched hash means the "graphics-only" change was not graphics-only, and that is exactly what you wanted to find out.

## 13. Ending a video

1. `[FIELD]` **Every cut ships with a closing CTA card, memes included.** Roughly 1.5 to 2s: logo, a follow line, the site. A video that simply stops on its last content frame feels abrupt and wastes the attention it earned.
2. `[CRAFT]` **Let the bed carry through the card.** Cutting audio dead at the seam is what actually makes an ending feel broken, more than the visual.
3. `[FIELD]` **The CTA is closure, not the mechanism.** Rule 1.8 measured that almost nobody reaches the tail, so the card is for the few who stay. Never park the pay-off there, and never let "there is a CTA at the end" substitute for building the ask into the first ten seconds.
4. `[CRAFT]` **Soft CTA only.** Follow, or the site. Codes and hard offers on an end card turn a shareable piece into an ad, which costs more reach than the offer wins.
5. `[FIELD]` **An end card cut from live footage is a segment, and it gets the full §9.10c in/out survey - constants escape the discipline BEATS enforce.** An outro anchored at "the frame where our banner sits centred" ran 2.8s into the camera's swing-away: by the card's last second a stranger's head filled the left foreground and the banner was sliced at frame right, and the founder spotted it on first watch. The beat table got frame surveys because every beat goes through them; the outro was a bare `OUTRO_IN` constant, so nobody sampled its tail. Survey the WHOLE card window (first, middle, last frames minimum) exactly like a beat, and pick the window off the steady stretch of the pan, not off the single prettiest frame.

## 14. Covers and thumbnails

0. `[FIELD]` **A purpose-built cover is part of the deliverable, on EVERY platform that
   accepts one. It is never an open item you offer to do later.** Shipping a scheduled
   video with "cover still to do" attached wastes the edit, because the cover is the only
   thing that decides whether the piece gets tapped at all. Build one per aspect ratio,
   composed from the master rather than grabbed from the delivery render (rule 11.10), and
   set it at schedule time: Instagram `coverImageUrl` at 1080x1920, YouTube `thumbnailUrl`
   at 1280x720 under 2MB. Where an API offers no cover image but does offer a frame
   selector - TikTok's `videoCoverTimestamp` - choose the frame deliberately instead of
   letting the default stand. Where a platform exposes nothing (Facebook, LinkedIn in
   Blotato), say so plainly rather than implying a cover was applied everywhere.

1. `[FIELD]` **Lay a cover out for the profile-grid crop, not just the 1080x1920 frame.** The grid square-crops a vertical cover to roughly y 420-1500, so a headline placed to clear the top UI band (y>330) gets decapitated in the grid. Everything that must be read - headline, subject, sub-line - has to live inside that centre band while still clearing the top UI. Landing the headline at y~430 satisfies both constraints; verify by actually rendering the square crop, not by trusting the arithmetic.
2. `[CRAFT]` **Pick the frame where the subject is looking at the camera.** Given a choice between a competent shot of someone working and an ordinary shot of them waving at the lens, take the wave. The cover's only job is to be tapped.
3. `[CRAFT]` **Crop out dead space before compositing.** Trade-show and office photos carry large empty walls and floors. Cropping to the subject and their props lets the photo card run bigger inside the same layout, which is the whole difference between a cover that reads at thumbnail size and one that does not.
4. `[FIELD]` **Do not let the headline repeat what the photo already says.** If the brand wordmark is legible in the shot, the headline's job is the thing the photo cannot say - where you are, or what is happening.

## 15. Driving a live product UI for screen beats

When the story is "here is the thing we built", the screens have to be the real ones. A designed mock of your own product reads as a designed mock, and the audience that would have believed the walkthrough is exactly the audience that spots it.

1. `[FIELD]` **Drive the real flow with a headless browser and screenshot each state, rather than rebuilding the UI in the design tool.** A scripted walkthrough gives you consistent framing, a rerunnable capture when the product changes, and states no static mock would bother to include. Capture at 2x device scale so a punch-in still resolves, screenshot the flow's own container element rather than the viewport so you get a clean card with no page chrome, and inject a stylesheet that hides popups, cookie bars and announcement banners before the first shot.
2. `[FIELD]` **Stop at any gate that would write to a production system, and design the beat around stopping.** A plan builder we were filming ends in a lead-capture step; completing it to reach the nicer final screen would have created a fake customer record and could have triggered the live follow-up messaging attached to it. No ad visual is worth writing fabricated rows into the CRM. Shoot up to the gate, and let the pay-off beat be real footage of the physical product instead of the screen behind the wall.
3. `[FIELD]` **A prefilled `value="0"` defeats the obvious "is this field empty" guard.** Skipping fields that already have a value is the natural way to write a form filler, and `"0"` is a non-empty string, so the age inputs stayed at zero and the flow refused to advance with a validation error that looked like a selector problem. Address known fields by explicit selector and use the automation library's real typing, which clears and fires the events the page is listening for, instead of assigning `.value` and hoping.
4. `[FIELD]` **Conditional controls make a naive click helper hang, not fail.** A confirm button that only appears for out-of-range input still exists in the DOM when it is hidden, so the click waits for visibility until it times out and takes the whole run down thirty seconds later, several steps from the actual cause. Check visibility first, cap every click with a short timeout, log the skip and carry on.
5. `[CRAFT]` **Make the state the voiceover claims visibly true.** If the line says the plan works around what your pet reacts to, that chip has to be selected in the frame, and the assertion is worth writing into the capture script rather than checking by eye. Same for coherence between fields: an input that contradicts a selection elsewhere triggers the product's own "are you sure?" warning, and you will screenshot the warning.
6. `[CRAFT]` **A real screen carries its own headline, so your label has to go somewhere else.** Positioning an eyebrow label by absolute y put it straight through the question each screen was asking. Compute the card's box first and place labels relative to it, above or below, never at a fixed coordinate chosen while looking at one screen.

## 16. Composing on an oversized plate

Building each beat as a larger still and cropping a moving window out of it is a clean way to get motion without `zoompan` (§12.1) and without a thirty-input overlay graph: composite every frame in the imaging library and hand ffmpeg a finished sequence.

1. `[FIELD]` **Content must fit the VISIBLE window, not the plate.** With a 1440x2560 plate feeding a 1080x1920 crop, anything wider than the crop is silently clipped at both edges, and a card centred on the plate is still centred after cropping, so it looks deliberate right up until you notice the screenshot has lost its margins. Size every element against the crop dimensions, then centre it on the plate.
2. `[CRAFT]` **Reserve the caption band before you place anything.** Decide the caption's y first and clamp the card's height so the two can never meet. A card sized to "as tall as it fits" will grow into the band the moment a source image is taller than the one you designed against.
3. `[FIELD]` **Trim trailing background off a captured screen before carding it.** A full-page capture of a short form is mostly empty page, and scaled to fit it leaves the actual content tiny inside a large blank card. Scan up from the bottom for the last row that differs from the corner pixel and crop there.
4. `[CRAFT]` **Auto-fit display type, not only captions.** §12.8 says this for captions; end cards break the same way and more visibly, because a wordmark is exactly the string you set once at a size that happened to fit and never re-measured. Shrink to the safe width, or force the wrap.

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
9b. Claims: does every caption assert only what the footage actually shows, and is the subject of each line on camera doing the thing that line describes? Any claim the transcript cannot back gets replaced with the speaker's own words.
10. Real-world numbers on screen (ratings, review counts, order counts) re-verified against their live source at build time - brand stats drift and a stale counter in a receipts beat undermines the whole receipt.
11. Source colour: if the raw file is HDR (`arib-std-b67` / `smpte2084`), was it converted through the OS tone mapper first? Was the render compared against a system reference still?
12. Speech density: what fraction of the timeline is someone talking? Under ~90% on a talking-head cut means there is still air to remove.
13. After shipping, write the session's learnings down TWICE, same session, before handoff: the project-specific version (real names, paths, open questions) into your own persistent notes, and the generalised version here, sanitized. They are different documents for different readers - copying one into the other loses either the specifics or the transferability. The rulebook only compounds if every build pays into it.
14. Rendering integrity: frame COUNT asserted against the sum of parts after every join (not duration, which a tolerance will wave through)? Frozen-frame scan run over the whole timeline? Any move on a still proven static by cross-correlation rather than by watching it?
15. Ending: CTA card present, bed carrying through it, and the ask also made inside the first ten seconds?
16. Redaction (if any real document is on screen): built default-deny, margins of every screenshot read for third-party names and spend, labels sharp and values killed?
16b. Scannable codes: every frame checked for a live payment/QR code caught in shot, covered with an opaque information panel rather than a blur, and that panel sized against the object's drift across the whole window rather than one frame?
17. Transcript: any hallucination loops (huge segment, few words, repeated token) caught and re-transcribed? Any word that resisted multiple decodes flagged rather than shipped as a confident quote?
18. Wordplay: every caption read aloud as a stranger would hear it, checked against well-known phrases it might echo? A line that scans well is exactly the kind that has a second reading.
19. Sound: if the cut is billed as ASMR or leans on natural sound, was the diegetic track band-measured rather than assumed present? No `dynaudnorm` anywhere near room noise?
20. Sources: `du -sh` (never `ls`) on every input before a rebuild, and anything showing 0B rehydrated first?
18. Finished render re-transcribed and diffed against the intended caption list, and the diff's DELETE opcodes driven to ZERO? (The similarity score is not the gate - it sits in the 90s while a caption asserts words nobody said.)
19. Every composited cutout fully inside frame, outlined, and rendered UNDER the caption layer?
20. Captions: does any chunk straddle a cut, and is every emoji legible against the background it actually lands on?
21. Beats: has any deliberate setup pause been trimmed away by the speech-density pass? A punchline needs its air back.
22. Every source clip run through volumedetect, so no dead-mic take is sitting in the timeline and no `"Thank you."` transcript was taken at face value?
23. Every trimmed segment checked for caption chunks that straddle the new out-point and still print words you cut?
24. The tail frames of each take looked at, not just the word timings? A presenter who breaks character right after the last word means the cut belongs one word earlier.
25. Format E only: cutout present from frame one and on every card beat, one message block per card, receipt crops uncut, head-clearance computed, bed + SFX mixed, CC-BY credit in the caption?
26. Names dictionary applied to this build's captions (Nic, not Nick), and any new proper-noun correction from this session added to the shared list?

## 17. Session additions - 2026-08-15 (three-reel batch: price-rise + two plan-flow walkthroughs)

1. `[FIELD]` **A segment boundary that lands inside a word's span silently deletes it from the captions.** The caption filter keeps only words fully inside a segment's audio window, so a cut at 16.10 through a word spanning 15.50-16.18 drops it - and it was the hook number ("$1.70"). Whisper had also split the number into two tokens ("$1" + ".70"), which is what pushed its end past the cut. Two rules: merge currency/decimal token splits in the transcript-fixes layer BEFORE planning cuts, and check every planned boundary against the word list for straddles.
2. `[FIELD]` **ffmpeg `tile` fed a glob of mixed-size PNGs emits one frame and stops, silently.** A contact sheet built that way shows only the first thumbnail on black - it looks like footage is missing when nothing is. Normalise sizes first or just tile with the imaging library, which also gives you index labels for free.
3. `[FIELD]` **Element screenshots taken under a sticky header carry the header baked over the element's top.** Hide the header (and any sales-pop / recently-purchased / discount-toast app, by CSS pattern) BEFORE the first capture; a mid-page toast bakes into a full-page capture exactly where the crop was going to land.
4. `[FIELD]` **Verify the SPECIES/subject of every montage clip by frame, not by folder.** A clip pulled from the cats folder by UUID landed a puppy as the closing shot of the cat ad. UUID filenames are content-blind in both directions.
5. `[FIELD]` **On-demand cloud placeholders (`st_blocks == 0`) can take 30+ minutes per folder to hydrate.** Kick hydration of every candidate folder at session start, survey only files with local blocks, and design beats around what is actually on disk - the plan-B for the beat is chosen for you if you don't.
6. `[FIELD]` **A silent source clip run through an `-af` chain produces a segment with NO audio stream, and the concat filter then fails cryptically** ("Stream specifier ':a' matches no streams"). Probe `has_audio` per clip and map an anullsrc when absent - same trap as the two-audio-tracks bug, opposite direction.
7. `[FIELD]` **A shipping label in your own founder's hands is a live tracking QR plus a customer address - same class as a booth payment QR.** A "carrying boxes" b-roll beat shipped to QA with a parcel label facing camera; the QR decoded (at 1x, no upscale needed) to a real consignment tracking number. Cheapest fix was rule 11.12's: a different window of the same clip with the label facing away, which also happened to be the better shot (the cold-chain truck in frame). Scan every frame where a parcel, envelope or label is legible, not just event signage.
8. `[FIELD]` **Search talent by NAME across the whole library before concluding footage doesn't exist - rule 3's filename trap has a folder-shaped twin.** "No Lola clips" was concluded after surveying two eating-clips folders; the library had an entire `04_talent/Lola/Feeding Lola POV` shoot. The named subject of a line gets a library-wide name search (folder names, not just file names) before any stand-in is cast, and the founder's "it's definitely in the NAS" is a search directive, not a hope.
9. `[FIELD]` **A standing names dictionary is part of the transcript-fixes layer, and it persists across videos.** Whisper hears "Nic" as "Nick" every single take, and the wrong spelling reached burned-in captions twice in one day because the fix map lived in one build script instead of everywhere. Proper-noun corrections (people, brands, pets) belong in a shared fixes list applied by every build, and each new correction the founder gives gets added the same day. Current list: Nick->Nic, cable->kibble, fuzziest->fussiest, pet->pack (when the subject is a parcel/delivery - see section 18.4).
10. `[FIELD]` **A small intrusion at a frame edge (a finger, a cable, a foot) is a crop, not a reshoot.** The founder liked the clip and hated the finger. Zoom ~1.15-1.2x with the crop anchored AWAY from the intrusion edge (crop y=0 to cut the bottom) and the clip survives. Check the re-crop against faces and the safe zones like any other frame change.
11. `[FIELD]` **Montage clips with noisy room audio get MUTED under the bed, not ducked.** A 0.35-gain "diegetic" track that is actually aircon and handling noise reads as static (-35dB of hiss at 44s got flagged within minutes). Rule 5.8 already says measure before promising ASMR; the corollary is that when the measurement says noise, the clip contributes zero audio and the bed carries the moment.
12. `[FIELD]` **When the founder says "we talked about this before", the correction was taught and never written down - that is a process failure, not a memory failure.** Chat sessions die; the repo survives. Any correction given twice means the first occurrence was not paid into the rulebook the same day it happened. The self-learning loop (§9 of PLAYBOOK.md) is the contract: write it down BEFORE handing off the video, not after the next session relearns it.

## 18. Session additions - 2026-08-25 (event founder interview, locked-off two-shot)

1. `[FIELD]` **Attribute speakers by measuring mouth motion, not by guessing from register.** A
   two-hander interview needs to know who said what before a single cut is planned - it decides
   which single you punch into, which quote the caption attributes, and whether the post caption's
   "he said" is true (rule 7.13's twin, for audio instead of wardrobe). Crop a mouth-region ROI per
   speaker out of the master, decode at 10fps greyscale, take the mean absolute inter-frame diff,
   normalise each channel and compare per transcript segment. On a 193s two-founder take this
   produced two clean contiguous blocks that matched the handover line in the take ("Nic?" / "yeah,
   you can start first") with no ambiguity. It costs one ffmpeg pass per speaker and removes the
   entire class of mis-attributed quote. Interjection segments under ~1.5s come back with tiny
   margins - treat those as unresolved rather than as findings.
2. `[FIELD]` **A 4K vertical master makes the punch-in free, so cut video per SHOT and audio per BEAT.**
   Shooting 2160x3840 means a 1080x1920 "single" is a 1:1 native crop, not an upscale - one locked-off
   two-shot yields wide, two-shot, and a tight single of each speaker at full resolution. Build the
   two streams on different grids: audio concatenated per BEAT (one continuous run of speech, so no
   join ever lands inside a sentence and the click/chopped-word class cannot occur) and video
   concatenated per SHOT (reframes that change every 2-3s inside that continuous audio). An assert
   that the two timelines agree to the frame is what keeps them honest. This gets rule 2.4's "visual
   change every 3-5s" for free on a single static camera.
3. `[FIELD]` **A badge position that clears every face in a single clears none in a two-shot.** The
   house top-left badge at y~370 sat squarely on the frame-left founder's chin the moment the cut
   pulled out to hold both people, because a framing containing two seated subjects puts a head in
   both top corners. Moving it to top-right just swaps which face it lands on. Derive badge windows
   from the shot list - show it only over single framings, hide it over any framing that holds more
   than one subject - rather than picking one coordinate and hoping. Same logic as hiding it over a
   full-frame proof card.
4. `[FIELD]` **Whisper hears "pack" as "pet" in a pet-food interview, and context makes the error
   invisible.** "If your pet comes slightly defrosted" reads as a plausible sentence in a transcript
   about animals, which is exactly why it survives review; four isolated decodes (two speeds x two
   temperatures) all returned "pack". The full-take pass is the optimistic one (rule 9.10b) and a
   domain vocabulary the decoder half-knows is where it leans hardest. Any noun that is load-bearing
   AND has a near-homophone inside the brand's own vocabulary gets the isolated decode before it is
   burned in. Added to the standing fixes list.
5. `[FIELD]` **The master re-transcribe diff is nearly free on an overlay-only re-render - prove the
   audio hash instead of re-running Whisper.** Caption legibility, badge windows and text-case fixes
   all re-render graphics over an untouched audio chain. Decoding both renders to raw PCM and
   comparing a hash takes about a second, carries the earlier zero-deletes verification over intact,
   and (per rule 12.16) tells you immediately if a "graphics-only" change quietly was not.
6. `[FIELD]` **A chunker that caps at N words butchers phrases; break at the widest gap instead.** A
   hard 5-word cap produced "We actually let you keep" / "it and pass it to" - breaks mid-phrase that
   read as a transcription bug. Chunk in two passes: hard breaks first (beat change, terminal
   punctuation, pause > 0.30s), then recursively split any run still over the cap **at its widest
   internal gap nearest the middle**. Then absorb any surviving one-word or sub-0.34s chunk into its
   neighbour in the same beat - otherwise the short-chunk filter silently drops a spoken word from
   the captions ("the dog doesn't like" / "you have leftover packs", with the "it" gone).
7. `[FIELD]` **Capitalise the first SURVIVING caption of each beat, after filtering, not before.** A
   0.12s "I mean," opened a beat, got capitalised, and was then dropped by the minimum-duration
   filter - leaving the beat opening on a lowercase "the". Any pass that removes chunks invalidates a
   cosmetic pass that ran before it.
8. `[FIELD]` **Cream captions with a brand-colour stroke disappear on event footage.** The house
   caption recipe is tuned for kitchen and studio backgrounds; a convention hall gives you white
   tees, pale banners and a bright metal fence, and 66px cream-on-teal-stroke read as thin grey
   smudge at thumbnail size. A filled teal pill at ~84% opacity behind 80px text fixed it in one
   render. Judge caption contrast against the actual background of the actual shots, not against the
   palette.
9. `[FIELD]` **`ls` says gigabytes, `du` says 0B, and the network tells you why.** Rule 12.15 covers
   eviction; the sibling failure is a sync client reaching the NAS over a *relay* instead of the LAN.
   The tell is the local address: a 172.20.10.x client IP is an iPhone hotspot, and the transfer ran
   at 158 KB/s (36GB = 64 hours) against 16 MB/s once the machine was back on wifi - a 100x
   difference that no amount of parallelism fixes. Measure throughput with two `netstat -ib` samples
   before designing the session around a hydration plan, and check the client IP when it is slow.
   Parallel `cat` across five large files during a network switch also returns "Operation timed out"
   with a zero exit from the loop, so wrap hydration in a retry and re-check `du` afterwards rather
   than trusting the loop finished.

## 19. Session additions - 2026-08-27 (scheduling a filmer's supplied edits)

1. `[FIELD]` **A supplied edit from a professional filmer still gets the full frame survey,
   and the thing it hides is camera movement.** A polished, captioned, branded cut opened
   with a 1.8s handheld whip pan (operator swinging from a close-up to the two-shot, kept
   in as a "transition"), and the founder flagged it on first watch - the THIRD shake
   flag across sessions. Editors normalise their own camera moves; founders reviewing on
   a phone do not. Survey the head of every externally-supplied cut at ~5fps before
   accepting it, and treat any whip/settle inside the first 6 seconds as a defect, not a
   style choice.
2. `[FIELD]` **The trim that removes a shaky open often uncovers a better hook.** The
   swing sat between banter ("hashtag no regrets") and a confession ("we don't
   communicate on very small stuff"). Cutting to the settled frame lost the banter and
   opened cold on the confession - which is the stronger opening by the hook rules
   anyway (1.2: confession beats greeting). When a defect trim and a hook upgrade point
   at the same in-point, take it without mourning the trimmed material.
3. `[FIELD]` **Verify a mid-speech in-point by isolated decode at MULTIPLE candidate
   offsets, not by the word timestamps.** Whisper stretched "we" across 4.72-5.68s (it
   was leaning on the neighbouring words), which made every candidate cut look like it
   chopped a word. Decoding 4s windows at three in-points 150ms apart returned the same
   clean sentence from all three, proving the true onset sat later than the label. The
   label lies; the isolated decode is the honest pass (same mechanism as rule 9.10b).
4. `[FIELD]` **Never transcribe the same source twice - cache word timings next to the
   footage.** A 28-minute shoot is ~10 minutes of mlx-whisper, and every new job that
   touches the same footage pays it again. `templates/transcript_cache.py` keys the
   whisper JSON by `sha1(basename|size|mtime)` into `SynologyDrive-sync/_transcripts/`
   with an `index.csv`, so `get` is free on a repeat, `grep` searches every clip ever
   transcribed at once, and a re-encode (which changes the fingerprint) correctly
   re-runs. **`grep` across the whole cache is the real win**: it found the pricing and
   transparency soundbites for the Aug-2026 price reel across two different interview
   files in seconds, including the one the delivered edit had thrown away.
5. `[FIELD]` **Prefer the RAW interview over a filmer's finished cut when the video needs
   its own argument.** Yongnan's `Founders Pay.mp4` was fully finished (burned captions,
   sticker intro, pinned banner), so its captions could not be retimed and its subject
   was fixed. The raw `Interview/` files carried the SAME answer in a cleaner take ("Fun
   fact, we have not taken a single dollar out of this business yet" - a better hook than
   the line that survived into the delivered cut), plus a second location. Use the
   supplied cut when you want the filmer's video; use raw when you want a different one.
6. `[FIELD]` **Two captions enabled on the same frame render as garbled overlapping text.**
   Clamping each caption's end to `min(own_end + tail, NEXT chunk's start)` before the
   2-frame gap is what fixes it. Subtracting 2 frames from your own end is NOT enough -
   the next chunk can start before your padded end, and the proof frame showed
   "sing  business yet.  this" from two pills stacked. Also join tokens that start with
   a hyphen onto the previous word, or whisper's "co" + "-founder" prints as "co -founder".
7. `[FIELD]` **Assert that type fits the frame instead of eyeballing a contact sheet.**
   A 122px Fredoka CTA measured 1092px wide in a 1080px frame and bled off both edges;
   it was only obvious once measured. Every headline draw now runs
   `assert tw < W - 80`, and the cover build asserts the whole type block ends above the
   IG profile-grid bottom (y1500). The cover assert fired on the first run at y=1625.
8. `[FIELD]` **A logo that is one flat colour disappears on a ground of that colour.**
   `circle_icon_only.png` is dark green on transparent, so it vanished entirely on the
   green end card and read weakly on busy footage. Always composite the mark on a filled
   cream/teal disc rather than pasting it bare, at both badge and end-card sizes.
9. `[FIELD]` **Cutting from live room tone to `anullsrc` silence reads as a broken file.**
   Card beats should carry their b-roll's own event ambience ducked to ~0.18 rather than
   digital zero. Tell: the master re-transcribe hallucinated a sentence on loop over the
   silent stretch, which is a useful smoke alarm for dead audio in the gate-3 diff.
10. `[FIELD]` **Verify every on-screen number against the LIVE page, not the KB doc.**
   The price reel's `$8.81 / $7.10 / $1.71` were confirmed by curling
   `/pages/transparent-pricing` cache-busted and matching the exact string, and the
   deadline weekday was confirmed with `datetime` rather than trusted from prose. A
   published price is the one claim in a reel that cannot be quietly wrong.

## 20. Session additions - 2026-08-31 (hook surgery on a filmer's burned-caption cuts, six-piece schedule)

1. `[FIELD]` **Measure each supplied cut's sticker preroll separately; it is not a constant.**
   Three cuts from the same filmer and the same shoot carried 3.76s, 4.00s and 6.32s of
   "founder series" sticker before the first usable frame. On the long one the speech
   ("we are friends, we are friends") had already started under the sticker, so the in-point
   moved to the next sentence, which was the stronger cold open anyway (rule 19.2 again). A
   4s trim applied by assumption would have shipped the third cut opening on a sticker.
2. `[FIELD]` **When captions are burned in, the hook lives in the band between the filmer's
   pinned banner and the heads.** A cream pill with teal Fredoka type, 64px, held 3.2s with a
   0.3s alpha fade, at y~368 on 1080x1920 for a one-line banner and y~402 for a two-line
   banner. Proof-frame it per cut: the first pass overlapped the banner on two of three cuts
   and the two-line banner on the third, and both were invisible until composited.
3. `[FIELD]` **Blotato rejects Instagram captions with more than 5 hashtags** ("Instagram
   allows a maximum of 5 hashtags per post"), and the rejection only comes back at schedule
   time, so a batch of 30 loses its IG reels silently unless every result is read. Cap IG at 5
   in the caption doc; TikTok and YouTube take more.
4. `[CRAFT]` **Schedule the reel's IG Story two hours after the reel, not at the same
   minute.** The story card says "new reel on the feed"; it has to be true when it is seen.

## 21. Session additions - 2026-09-20 (collab interview off a Telegram re-compress)

1. `[FIELD]` **Attribute a two-hander by PITCH, not by mouth motion, whenever one person is
   reacting.** Rule 18.1's mouth-ROI pass called the best line in a take for the wrong speaker
   by a decisive 1.78-vs-0.97 margin, because the man was laughing through the whole 3.2s
   window while the woman delivered it. A median-f0 pass over the same window settled it in
   one shot: her known beats ran 205-208 Hz, his 131 Hz, and the disputed window read 271 Hz -
   her, pitched up because she was doing an impression. Mouth motion answers "whose face is
   moving", which is not the question. Measure f0 first, and keep mouth motion for the case
   where both voices sit in the same register. Autocorrelation over 1024-sample windows above
   an RMS floor is about ten lines and needs no model.
2. `[FIELD]` **A rounded shot boundary inside a beat can leave a 1-frame orphan span, and the
   concat filter eats it.** Cutting video per SHOT inside audio cut per BEAT (rule 18.2) means
   two independent roundings - `frames_of(beat_dur)` and `frames_of(shot_rel_out)` - and when
   the last shot's rounded end lands one frame short of the beat's, you get a 1-frame segment
   at the seam. Every per-segment frame assert passes, then the join comes back one frame
   light and the §12.11 total assert is the only thing that catches it. Absorb any interval
   under 2 frames into its neighbour when building the mark list, rather than hunting the
   off-by-one afterwards.
3. `[FIELD]` **A near-zero word timestamp on a load-bearing noun means cut the clause, not
   caption it carefully.** Rule 9c covers the two-speakers-at-once case; the same 0.00s span
   shows up on a single speaker when the decoder is guessing. "There isn't any sort of ???
   repository" split four passes between "central" and "essential" with the word timed
   85.66-85.66. The fix was not a fifth decode: the other founder had already said the same
   thing cleanly ("collate all this in one centralised place"), so the whole clause went. Rule
   10d's restatement search applies to undecodable words, not just to unusable pictures.
4. `[FIELD]` **A video that arrived over Telegram is a 720p re-compress, and the xattrs say
   so.** `xattr -l` returns `com.apple.assetsd.creatorBundleID: ph.telegra.Telegraph` and the
   original filename. Telegram caps video sends at 720p unless the sender chose "send as
   File", so the ceiling on the edit is set before you open it: full-frame delivery is a 1.5x
   upscale and a single is ~2.6x. Both survive Instagram, but check provenance at the top of
   the session and ask for the File version before designing any beat around a punch-in.
5. `[FIELD]` **This machine's ffmpeg has no `drawtext` filter.** Labelled contact sheets die
   with "No such filter: 'drawtext'" mid-loop. Tile the frames in known order and label in PIL,
   or skip the labels.
6. `[FIELD]` **Snap every cut to a measured RMS valley, not to a Whisper word boundary.**
   Rules 5.x already say Whisper underestimates word ENDS; the sharper failure is that it also
   mislabels the next word's START, and the two errors together invent a gap that is not there
   or hide one that is. On the beat that shipped and got flagged, "giveaway" was labelled
   ending 120.52 and the following "So" labelled starting 120.52 - no gap, so the cut went in
   at 120.60 on the usual small tail. The envelope said otherwise: she was still at **-9 dB
   through 120.72** and the next sentence did not start until **121.08**, a real 0.35s valley
   that the transcript had erased by starting "So" 0.56s early. The cut landed mid-vowel and
   the founder caught it on first watch. Decode the whole take once to a 10ms RMS envelope,
   then for every planned boundary print the dB AT that boundary: anything above about -20 dB
   is inside speech and is a defect, whether it is an out-point chopping a word or an in-point
   carrying the tail of the previous one. Snap to the deepest valley in a +-0.5s search window.
   This is a ten-line check over the whole beat table and it is the only thing that catches the
   class, because a frame sheet cannot show it and the §12.9 deletes gate passes clean - the
   word IS present in the master, just amputated.
7. `[FIELD]` **Some cuts have no clean out-point, and the honest move is to say so.** The same
   envelope pass flagged a second boundary where the speaker ran her punchline straight into
   the next sentence with no valley anywhere in the following 0.6s. There was no fix that did
   not either strand a dangling fragment or eat the punchline, so it shipped unchanged and
   named in the handoff as unresolved. Do not burn two rebuilds hunting a valley that the
   performance never produced; measure, fix the ones that are fixable, and flag the rest for
   the person who can hear it.
