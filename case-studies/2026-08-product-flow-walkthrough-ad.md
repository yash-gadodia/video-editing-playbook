# Product-flow walkthrough ad: real screens, scripted VO

**Build:** two vertical ads (one per species variant) walking a viewer through our own onboarding flow. ~27s each, scripted VO over real captured product screens, word-timed captions, brand end card.

**Why this shape:** the ask was creator UGC, a real customer filming their own phone as they use the flow. We could not book creators in time and we would not synthesise the customer, because an AI-generated person presented as a real user is a fabricated testimonial and the campaign's entire angle is honesty. Scripted VO over genuinely captured screens says the same thing without anyone pretending to be anyone.

## What worked

**Capture the flow, do not rebuild it.** A headless browser walked the real onboarding wizard end to end and screenshotted each state at 2x. Screenshotting the wizard's own container element rather than the page viewport gave clean cards with no site chrome. Rerunning the script after a product change regenerates every screen, so the ad is cheap to keep current.

**Let the TTS give you the timings.** The voice API's with-timestamps endpoint returns per-character alignment, so word timings come back with the audio and there is no transcription round trip and no drift between what was said and where the captions think it was said. Every beat boundary in the build is an anchor phrase looked up in that word list, so a script fix re-times the whole edit for free. An assert that the resolved anchor indices are strictly increasing catches a mistyped anchor immediately.

**Composite frames yourself.** Nine beats with drift, an eyebrow label, a logo badge and about thirty caption chunks would have been a thirty-input ffmpeg overlay graph. Compositing each frame in the imaging library and handing ffmpeg one finished sequence was less code, fully deterministic, and sidestepped both the `zoompan` shake and the image-sequence overlay freeze.

## What the QA gate caught

Three defects, none visible from the build log, all obvious the moment frames were pulled at every beat:

1. The eyebrow label sat at a fixed y and landed directly on each screen's own headline. Every screen asks a question; the label was covering the question.
2. Cards were composed 1120px wide on a 1440px plate feeding a 1080px crop, so both edges of every screenshot were clipped. Centred on the plate, still centred after the crop, and wrong the whole time.
3. The end card wordmark was set at a size that fit the plate and overflowed the frame.

A fourth came out of the fixed version: with the card pinned below the eyebrow, short screens left a large dead band above the caption. Centring the card in the band between eyebrow and caption fixed it.

## The one that was not a rendering bug

The flow ends at a lead-capture step, and the portion result we wanted for the pay-off beat sits behind it. Submitting it would have written a fabricated customer into the production CRM and potentially fired the live follow-up messaging attached to that record. We shot up to the gate and used real footage of the physical product as the pay-off instead. Worth stating plainly because the temptation is real and the cost is invisible until someone finds a fake lead in a report.

## Traps worth remembering

- A prefilled `value="0"` is a non-empty string, so an "only fill empty fields" guard skips it and the form refuses to advance with an error that reads like a broken selector.
- A conditional confirm button that is hidden rather than absent makes a naive click helper wait for visibility until it times out, killing the run thirty seconds later and several steps from the cause.
- Selections the voiceover asserts have to be verifiably selected in the frame. Assert it in the capture script; do not check by eye.
- Field values that contradict each other trigger the product's own "are you sure?" warning, and you will screenshot the warning.
