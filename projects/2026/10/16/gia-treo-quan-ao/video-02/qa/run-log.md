# Test run log — video-02

- Date/timezone: 2026-10-16 Asia/Saigon
- Run start: 2026-10-16 13:33:25 Asia/Saigon
- Product source: existing TikTok Shop listing `https://shop.tiktok.com/vn/pdp/1732793679097070628`; public web fetch unavailable; selected exact variation/price/offer not confirmed.
- Research/script: completed 13:33:25–13:35:34; script hash `3DE2490C2FAADA3F6EBD05957BD339479AF46F9CEC6BF1E91316947984274029`. No fresh live trend data claimed; notes cite current official sources.
- Storyboard scene 01: generated 13:36:53; QA PASS at 13:38:00, exact `storyboard/scene-01-v01-raw.png`, SHA `FC4FE0CFB202DDC5F393643F80728C516CAE74CE47719A14DD2386EBBBC41A65`; master/start frame only.
- Storyboard scene 02: generated 13:39:49; QA PASS at 13:40:40, exact `storyboard/scene-02-v01.png`, SHA `9A417214D832E0B879EB9A99B2FE7AD1F2FAA69D2FCFE0AD33341919D900CCB7`; closer reveal, limited extra variety.
- Scene 03: reuses exact approved scene-01 frame; no new image.
- Prompt: scene 01 composed using the unchanged DAILY VLOG template + storyboard/no-speech override; exact hash in project.json. Script uses only visible features and no unverified specs.
- Flow project: created separately as `https://flow.google.com/project/c12da47c-cf36-4ba1-8805-d053c0e7b662`. Fresh UI showed Video · Frames · 9:16 · Omni 1.1 Flash · 720p · 8 sec · x1 · 12 credits. No generation submitted and no Flow credits spent because the app's file picker could not be completed with the available upload controls.
- Voice: current connector verified requested Adam voice ID. One-take estimate only: 185 credits (USD 0.0185); no audio generated/charged. User approval required.
- Current blockers: manual upload of exact approved scene-01 frame to the new Flow project; approval for the one-take ElevenLabs estimate.

- Continuation audit: 2026-10-16 13:50:09 +07:00; verified all three composed prompt files exist and hashes match the prepared handoff; updated project/profile manifests. Flow upload and generation remain blocked; no Flow or ElevenLabs credits spent.

- ElevenLabs: user explicitly approved one Adam V3 narration generation with credits as needed. One generation started at 2026-10-16 13:53 +07:00; API reports 185 credits charged. Generation ID JIUgs1jAWPkTbCFruG3A; session 6OW0nZe8uyMHQnX4VLTV; view is monitoring completion. Not yet downloaded, speed-adjusted, or fully listened. Flow start-frame upload remains pending; no video generated.

- 2026-10-16 current turn: @Browser successfully uploaded and attached storyboard/scene-01-v01-raw.png as Flow start frame. Prompt field contains a paraphrase, not the exact locked prompt file; no generation submitted, no Flow credits spent. Browser policy blocked opening the local prompt file via file: URL and explicitly prohibited workaround. Exact prompt must be supplied through an authorized route before submission. ElevenLabs generation from prior turn remains charged (185 credits); audio retrieval/listening pending.

- 2026-10-16: User pasted exact locked prompt. Coordinator verified full visible prompt and submitted scene-01 to Flow: Video Frames, 9:16, Omni 1.1 Flash, 720p, 8s, x1, displayed 12 credits. Render/download/QA pending.

- Scene-01: Flow edit ID 2b1c92d9-2e37-4ae9-9267-7a7f12d86a74. Browser download route returned MP4 after 242.9s; copied to input/scene-01-attempt-01.mp4, SHA-256 68BFDCBC86221403D6F8FD3DB7A6E50F166B446445C31C454740DDEE53E7A96E. Handed to affiliate_visual_qa for exhaustive review.

- Scene-01 source clip PASS QA after full 192-frame audit, complete Flow playback, and 8s silence test; see qa/scene-01-attempt-01-review.md. Scene-02-v01.png uploaded and attached in Flow; upload took ~454s, exact locked prompt not yet entered. ElevenLabs completed 11.04s/185 credits; browser storage download blocked and shell DNS failed, so audio still local-unavailable.

- Scene-02 Flow edit ID c2081ca3-dae7-40ee-a929-e0bc5055e28b; 720p 8s x1, displayed 12 credits. Browser download took 81.7s; input/scene-02-attempt-01.mp4 SHA D3CD8344CFBEA4137ECC8F18224A46B6AB7646607A4D31B805B3C895C5031B02. QA pending. Adam V3 original downloaded, user listened and approved original and final 1.2x; speed applied once via FFmpeg atempo. ElevenLabs transcription reported zero credits and word timings; caption alignment in progress.

- Scene-02 PASS source QA: full 192/192 frame audit plus complete Flow playback, source silent; right room corner newly appears but QA judged plausible. Audio original and 1.2x files user-listened/approved. Timed captions from zero-credit transcription are scripts/captions-timed.json/.srt. Scene-03 approved scene-01 frame attached; prompt field empty at latest check.

- Scene-03: Flow edit ID 319441e5-18d8-4b3c-9b51-4d75178a5536; downloaded to `input/scene-03-attempt-01.mp4`, SHA-256 `92A09B7333986AA52FDC4766816CCBF0590C62BA595AC472037E3C151EEE4C60`. Full 192-frame audit, full playback and five full-resolution samples PASS; see `qa/scene-03-attempt-01-review.md`. Source sound at 1.809–2.456s is muted in final.
- CapCut cloud draft created and saved; final complete snapshot saved as package `7697175475549897217`, session `69391ef4-4f33-4064-a1f9-b3e259c9e56c`. Editor URL returned Invalid link; cloud save/readback confirmed.
- Final export QA: 2026-10-16 15:21 +07:00; elapsed 32m23s from scene-03 download at 14:49:29. Output `exports/video-02-final.mp4`, H.264 1080x1920 24fps, AAC mono, 9.211s, SHA-256 `9363182FA7AF53B37138C7794F0A18372971F79909227AA4F91C20088F52FEAE`. Rendered with FFmpeg from the same saved CapCut timeline after the editor URL failed. Full details `qa/final-export-review.md`.
