# The locked-off two-shot: measure who is talking, then cut video and audio on different grids

**Build:** a 45s cut from a 193s founder Q&A shot at a pet expo. One camera, locked off,
2160x3840 vertical, both founders seated and mic'd. Brief: "make a super excellent 45s ish
video... high chance to perform well on ads and go viral."

Two problems define this format. You do not know which founder is speaking at any moment,
and a static wide two-shot has no cuts in it. Both turned out to be measurable rather than
matters of judgement.

## Who is talking is a measurement

The temptation is to infer the speaker from register - one of them says "I mean" and
"right?" a lot, so segments full of those are probably his. That is a guess, and everything
downstream inherits it: which single you punch into, which quote a caption attributes, and
whether the post caption is true.

Instead: crop a mouth-region ROI per speaker straight out of the master, decode at 10fps
greyscale, take the mean absolute inter-frame difference, normalise each channel, and
compare the two over each transcript segment. One ffmpeg pass per speaker.

The result was two clean contiguous blocks - one founder 27-125s, the other 127-192s - and
it independently reproduced the handover that is audible in the take ("Nic?" / "yeah, you
can start first"). Segments under about 1.5 seconds came back with margins near zero; those
are genuinely unresolved and were simply not used as attributed beats.

## 4K vertical makes the punch-in free

At 2160x3840, a 1080x1920 window is a 1:1 native crop. So a single locked-off camera
actually contains five shots: the wide, a two-shot, and a single and a tight of each
speaker, all at full delivery resolution with no upscale anywhere.

That suggests an architecture. Build audio and video on **different grids**:

- **Audio concatenates per BEAT** - one continuous run of speech per beat, so no join ever
  lands inside a sentence. The click and chopped-word failure classes become structurally
  impossible rather than merely checked for.
- **Video concatenates per SHOT** - 17 reframes changing every 2-3s *inside* that
  continuous audio.

An assert that the two timelines agree to the frame keeps them honest. This buys the
"visual change every 3-5s" rule on a camera that never moved, and the 42.8s of speech came
out at 95% density with nine jump cuts nobody has to hear.

## The badge has no single safe corner

The house rule puts the logo badge top-left at y~370, which clears faces in every single
framing. The moment the cut pulls out to hold both founders, it lands on the frame-left
founder's chin - because a framing containing two seated subjects has a head in *both* top
corners. Moving it to top-right just changes whose face it covers.

The fix is not a better coordinate, it is deriving badge windows from the shot list: show
it over single framings, hide it over anything holding more than one subject. Same logic as
hiding it over a full-frame proof card, and it generalises to any multi-subject cut.

## "Pet" and "pack" sound the same to a decoder that knows the topic

The full-take transcript read "if your pet comes slightly defrosted". That is a plausible
English sentence in a transcript about animals, which is exactly why it survives a read.
Four isolated decodes - two speeds, two temperatures - all returned **"pack"**, which is
also the only reading that makes sense.

The general shape: a decoder leans hardest where it half-knows the domain vocabulary. Any
load-bearing noun with a near-homophone inside the brand's own vocabulary gets the isolated
decode before it is burned into a caption. It went into the standing fixes list, because
this speaker triggers it every take.

## What the diff was actually for

The master re-transcribe diff came back at 0.974 with a single delete and three replaces.
The delete was a filler word the render-side decode dropped; the useful finding was one of
the *replaces*, which is the opcode the rulebook tells you to skim past. It was how the
pet/pack error surfaced at all.

Worth noting the diff got cheaper as the build went on. Caption legibility, badge windows
and text-case fixes are all overlay-only re-renders over an untouched audio chain, so
hashing the decoded PCM of both renders carries the zero-deletes verification over in about
a second - and would have said so loudly if a "graphics-only" change had not been.

## The session's real bottleneck was a phone hotspot

`ls` reported 36GB of footage; `du` reported 0B. That much is a known trap. What was not:
the sync client was reaching the NAS over a relay because the machine was on an iPhone
hotspot - the tell is a 172.20.10.x local address. Throughput was 158 KB/s, or about 64
hours for the folder. On wifi the same pull ran at 16 MB/s.

Two `netstat -ib` samples five seconds apart would have caught it in the first minute,
before any hydration strategy was designed around the wrong number. No amount of
parallelism fixes a 100x deficit, and parallel reads during the network switch returned
"Operation timed out" while the surrounding loop still exited zero.
