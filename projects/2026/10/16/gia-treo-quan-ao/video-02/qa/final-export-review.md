# Final export QA — video-02

- Review completed: 2026-10-16 15:21 +07:00. Production segment from scene-03 download (14:49:29) to final export QA (15:21:52): 32m23s.
- File: `exports/video-02-final.mp4`
- SHA-256: `9363182FA7AF53B37138C7794F0A18372971F79909227AA4F91C20088F52FEAE`
- Technical: H.264 1080×1920, 24 fps; AAC mono 44.1 kHz; 9.211 sec.
- Picture: Three Flow source clips were reported as passing per-frame product-identity QA; the scene-03 written report is absent. That gate did not test creative differentiation. Timeline cuts at 3.256s and 6.592s; muted all source clip audio, including scene-03 interval with non-silent source sound. Checked frames around both cuts for black frames or discontinuities; none observed. Product remains fully framed.
- Narration: ElevenLabs V3 Adam, requested voice ID `pNInz6obpgDQGcFmaJgB`; user listened to and approved original and pitch-preserving 1.2× track. Speed applied once before import; CapCut speed remains 1.0×. Final export AAC is derived from that approved track.
- Captions: Clean Vietnamese, no V3 audio tags; positioned top-center with dark backing. Sampled at 1.5s and 7.0s; text readable and product unobstructed. Logo sits lower-right inside the safe picture area.
- Audio stream: final export contains the narration track only; no source video audio.
- Assembly provenance: Complete CapCut cloud draft save/readback confirmed (session `69391ef4-4f33-4064-a1f9-b3e259c9e56c`, package `7697175475549897217`). The CapCut editor URL returned “Invalid link”; final MP4 was rendered locally with FFmpeg from the same saved timeline, not exported by CapCut.
- Limit: product listing fetch did not confirm exact selected variation, current price or offer. Script and overlay avoid price/spec claims; “chọn đúng phân loại” follows the user-approved script but the linked variation remains unverified. Images are generated staging and do not demonstrate real use or load capacity.

**Corrected result: TECHNICAL PASS; CREATIVE FAIL. The repeated scene composition does not meet the intended scene variety. See `qa/root-cause-review.md`.**
