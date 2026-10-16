---
name: affiliate-fashion-elevator
description: Build a TikTok outfit or elevator try-on video using one unchanged prompt passage from the user's Thay đồ thang máy section.
---

# Thay đồ thang máy

Read the [original section text](../../../workflow/assets/fashion-elevator-source.txt) and [prompt registry](../../../workflow/PROMPT-MODES.md). This section contains multiple independent prompts and actions. Select the exact source passage that fits the chosen clothing product and intended video format; if multiple passages are plausible, ask which one the user means. Copy the selected text without rewriting it into a fixed template asset, save its hash in one `video-profile.json`, and reuse it for every Flow-generated scene of that video. Vary only the scene-specific prefix. Use the parent `$tiktok-affiliate-video` workflow for the overall script, clip review, voice, and edit. Preserve the referenced person's appearance and garment details where the chosen source passage requires them.

## Audio default
Follow [voice policy](../../../workflow/VOICE-POLICY.md): the user selected ElevenLabs V3 Adam narration and CapCut assembly, with 1.2x narration playback. Current connector has no speed parameter: apply 1.2x once to the audio track in CapCut, preserve pitch, then align captions and listen to the final track. Flow produces storyboard-based visuals/optional ambience, no speech. Keep audio tags in V3 raw text only, never captions or Flow dialogue. Preserve immutable source templates and record explicit audio/storyboard overrides. Do not relabel historical audio.
