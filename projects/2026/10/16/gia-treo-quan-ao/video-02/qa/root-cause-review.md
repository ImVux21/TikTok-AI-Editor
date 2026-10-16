# Root cause review — duration and repeated scenes (video-02)

Review date: 2026-10-16.

## Findings

1. The three Flow source files are each 8.000 seconds. The final export is 9.211 seconds because the narration/audio timeline runs 9.212 seconds, and the three clips were trimmed to 3.256 + 3.336 + 2.619 = 9.211 seconds. The edit therefore uses only about 38.4% of each 8-second generated clip; the rest was discarded. The video is essentially ten seconds because its audio is ten seconds, not because the three clips were played in full.
2. The scenes repeat because all three prompts enforce nearly the same continuous full-product composition. Scene 01 permits only a slight push-in. Scene 02 permits only a slight horizontal drift and explicitly forbids zoom, angle change, crop, tilt, orbit, and cuts. Scene 03 deliberately reuses scene 01's exact start image and allows only a slight settle, forbidding zoom, angle change, crop and new content. Consequently, the generated footage has no purposeful shot-size or camera-angle changes.
3. The script also constrained the product to an empty static reveal: no verified use demonstration, clothing, hands, or other props. This made distinct action beats unavailable, but the prompts could still have created distinct safe compositions or deliberate detail shots inside the visible geometry; instead they explicitly ruled most of those out. Scene 02's planned pan toward the side hook was replaced by a prompt that only allowed subtle horizontal drift.
4. The source template `10-SECOND DAILY VLOG MODE` calls for roughly 5–8 motivated shots per ten seconds, but it was appended to each individual eight-second Flow scene. Prefix restrictions overrode that variety guidance, and the editor then cut each continuous source down to about three seconds. There was no scene-level edit plan enforcing meaningful difference between the three selected excerpts.
5. QA correctly checked frame-by-frame product identity, geometry, and continuity, but the pipeline treated those source clips as approved without a separate creative-diversity gate. Final QA checked resolution, captions, sound, watermark coverage, and hard cuts. It did not reject the repeated visual composition. Thus the earlier final-report label “PASS for technical export and visual review” overstated creative approval.

## Corrected decision

The file is technically valid, but it fails the requested creative objective of three meaningfully distinct scenes. Mark the current export **NOT APPROVED for creative QA**; retain it only as an audit/reference artifact. It should not be treated as the finished affiliate video.

## Required corrective path

Revise the scene plan and prompts before spending on another generation: specify three visibly distinct, still truthful framings/actions (wide opening reveal; controlled detail view that shows both rails and the side hook; return to wide CTA frame). Keep every visible product part accurate and do not invent use, load capacity, props, price, or claims. Set a whole-video duration intentionally, then align narration, clip windows and cuts to that duration rather than letting the narration length alone determine the edit. Add a creative QA gate that compares each scene's framing, movement and informational purpose before assembly.
