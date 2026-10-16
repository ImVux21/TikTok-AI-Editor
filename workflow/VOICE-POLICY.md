# Giọng đọc và âm thanh

## Quyết định hiện tại — 2026-10-16

Người dùng đã chọn **ElevenLabs V3 cho giọng, ghép bằng CapCut**, thay mặc định Flow speech trước đây. Quyết định mới này ưu tiên hơn mọi đoạn hướng dẫn cũ còn nhắc Flow speech. Flow tạo video từ storyboard đã duyệt, không tạo lời thoại/người nói; có thể giữ ambience phù hợp. Loại thoại tự sinh để không chồng giọng. Các clip/audio cũ giữ nguyên provenance lịch sử, không gắn lại thành ElevenLabs.

Đã nhận văn phong Adam tại [ADAM_V3_PROMPT_SPEC.md](ADAM_V3_PROMPT_SPEC.md): nhây tự nhiên, “mấy dợ / mấy ní”, viết số thành chữ trong lời đọc, nhấn chọn lọc, chốt “Dứt!” hoặc “Dứt lẹ!”. Chỉ dùng claim/giá đã xác minh; ví dụ bát đĩa không phải dữ kiện giá treo.

## Tạo lời đọc

- Model `eleven_v3`; voice ID người dùng chỉ định `pNInz6obpgDQGcFmaJgB` (Adam). Kiểm tra voice có sẵn trong tài khoản và dùng được với model trước khi báo chọn thành công. Không tự đổi voice/model khi lỗi.
- Ưu tiên một track narration cả video ngắn để giữ giọng liên tục. Scene chia theo ý nghĩa, mốc cut theo audio thực tế. Chuẩn bị ảnh/clip song song sau khi khóa script; hoàn thiện timing sau khi audio đạt.
- Giữ audio tags trong `voiceTextRaw`/payload V3, loại khỏi `cleanSubtitleText`. Không gửi chúng thành lời thoại Flow. Nếu chủ động chọn v2, strip tags trước TTS và ghi mất điều khiển bằng tags; không fallback âm thầm.
- Chuẩn bị offline bằng `python scripts/prepare_adam_voice.py --plan <creative_plan.json> --output <voice-plan.json>`. Công cụ chỉ tách raw/clean và ghép narration; chưa gọi API hay tạo audio. Sau đó dùng tích hợp ElevenLabs được hỗ trợ, ghi request ID, chi phí thực và nguồn file.
- Khóa API dùng cấu hình bảo mật; không ghi khóa thật vào source, prompt hoặc log. Chọn provider không tự cho phép mua gói/tín dụng hay thử lại không giới hạn.

## Tốc độ

Người dùng đã chốt **1.2×**. Kiểm tra connector ngày 2026-10-16: `creative_generate_speech` không có tham số speed; schema V3 chỉ hiện voice_id/language_code. Vì vậy đường mặc định hiện tại là tạo narration V3, rồi chỉnh riêng track trong CapCut ở 1.2× có giữ cao độ. Không ghi voice_settings.speed vào tool không hỗ trợ. Nếu sau này dùng API có speed đã xác minh và đã áp dụng 1.2 thì CapCut giữ nguyên, không nhân tốc độ lần nữa.

Đo audio sau chỉnh để chốt cut/caption; với playback rate hậu kỳ, thời lượng còn T/1.2. Giữ requested_speed=1.2, nơi áp dụng, applied_speed và audio QA tách biệt; cấu hình đúng chưa chứng minh đã chỉnh file hoặc giọng rõ. [Bằng chứng connector/voice](audit-20261016-elevenlabs.json) xác nhận đúng Adam ID có trong danh sách, chưa xác nhận chất lượng tiếng Việt hoặc một generation thành công.

Nếu bản nháp CapCut không có cách xác nhận giữ cao độ, dùng `python scripts/prepare_narration_speed.py --input <narration-goc> --output <narration-1.2.m4a>` trước khi nhập; script dùng FFmpeg `atempo=1.2`, kiểm tra thời lượng, lưu hash và chặn xử lý hai lần trên output có metadata. Import file đã xử lý vào CapCut ở speed 1.0. Nghe track cuối và căn lại caption. Chỉ chọn **một** đường áp dụng tốc độ cho mỗi run và ghi vào `project.json`; không suy luận rằng mọi CapCut draft đều giữ cao độ.

## Phụ đề và QA

Phụ đề dùng lời sạch và timing audio cuối. Nếu alignment chứa tags, lọc theo offset/span ngoặc kể cả khi tag bị tách qua nhiều token; giữ timestamps tuyệt đối của lời còn lại. Không zip text đã rút gọn với timestamp cũ. Tiếng cười/thở có thời lượng dù không có chữ, không dồn mất khoảng đó. Nếu alignment thiếu hoặc sai, nhận dạng/forced alignment trên audio cuối.

Nghe toàn bộ track: rõ tiếng Việt, đủ lời, không đọc tags/chỉ dẫn, không lặp/cắt chữ và không đổi giọng. Tags không bảo đảm diễn xuất chính xác. Audio tồn tại hoặc ASR khớp chưa chứng minh chất lượng nghe. Sau khi audio đạt, `affiliate_post` căn timing/caption, bàn giao CapCut cho editor. Final QA nghe và xem đúng bản xuất.

Ghi provider/model/voice ID và trạng thái xác minh, raw/clean script, file/hash audio, tốc độ/nơi áp dụng, timing scene, kết quả QA và chi phí trong `project.json`. Không thay nguồn giọng trên dự án đã xuất.
