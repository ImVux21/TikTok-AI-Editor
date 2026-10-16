# Văn phong Adam — đặc tả người dùng gửi ngày 2026-10-16

## Phạm vi áp dụng trong dự án

Đã nhận prompt văn phong. Dự án hiện dùng storyboard → Flow → CapCut; chưa tìm thấy `scripts/ai-director.mjs`, `scripts/tts-generator.mjs`, `SyncedCaptions.tsx` hoặc `package.json`. Những tên này trong đặc tả là điểm tích hợp của hệ thống Remotion được mô tả, chưa phải code đang tồn tại ở đây. Không báo đã tích hợp TTS/Remotion khi chỉ cập nhật hướng dẫn. Người dùng đã xác nhận ElevenLabs V3 cho narration, CapCut để ghép. Flow chỉ tạo hình chuyển động/ambience; không gửi lời hoặc audio tags cho Flow. Quyết định này thay mặc định Flow speech trước đây. Chưa tạo audio trong lượt cập nhật cấu hình này.

## Chỉ dẫn viết kịch bản

Viết lời TikTok tiếng Việt như đang tám chuyện: nhây vừa phải, vui, thân mật, câu ngắn, có thông tin hữu ích. Dùng tự nhiên “mấy dợ”, “các dợ”, “mấy ní”, “con dợ”; không nhồi tất cả vào từng cảnh. Cảnh cuối chốt đúng “Dứt!” hoặc “Dứt lẹ!”. Không tự gọi giọng này là đang hot/viral nếu chưa có dữ liệu xác minh.

- `voiceTextRaw`: số, giá, phần trăm, mã sản phẩm đều viết thành chữ tiếng Việt; không có chữ số. Không đơn thuần xóa số hoặc dùng regex thay từng chữ số làm sai nghĩa. Thiếu dữ liệu thì bỏ claim, không điền số mẫu.
- Dấu phẩy và `...` tạo nhịp kể; VIẾT HOA có chọn lọc phần cần nhấn. Không kéo dài lời để đủ số giây.
- Headline/giá trên màn hình được dùng chữ số ngắn gọn khi dữ kiện đã xác minh. Quy tắc không chữ số chỉ áp dụng lời đọc, không áp dụng metadata, thời gian hoặc voice ID.
- Nếu chọn `eleven_v3`, thêm audio tags tiếng Anh có chủ đích: ví dụ `[excited]`, `[whispering]`, `[playful]`, `[sighs]`. Không lặp cùng tag liên tiếp; không bắt buộc dùng hết danh sách. Tags là chỉ dẫn mang tính xác suất, cần nghe thật để duyệt.
- Các câu mẫu về men hai lớp, chống bám bẩn, dùng lò vi sóng, giảm bốn mươi phần trăm, giá hai trăm sáu mươi chín nghìn, “kẻo hết” không phải dữ kiện của sản phẩm hiện tại. Không sao chép vào script nếu chưa có căn cứ. Không dựng lời chứng thực “tui dùng rồi” từ ảnh AI.

## Tách lời đọc và phụ đề

Mỗi scene có `voiceTextRaw`, `cleanSubtitleText`, `onScreenHeadline`, cùng provenance cho claim. Sinh `cleanSubtitleText` từ raw bằng xử lý xác định, không yêu cầu LLM viết lại một bản dễ lệch nội dung.

```js
function stripAudioTags(text) {
  return text.replace(/\[[^\]]*\]/g, '').replace(/\s+/g, ' ').trim();
}
```

Kiểm tra ngoặc/tag cân bằng trước khi dùng; nếu còn `[` hoặc `]` thì báo lỗi để sửa, không đẩy phụ đề lỗi vào renderer. Giữ nguyên lời, dấu câu và viết hoa. Chuỗi cho model hỗ trợ tags có thể giữ tags; chuỗi cho v2/Edge/Flow phải bỏ tags khỏi lời thoại, mô tả diễn xuất tách riêng trong phần chỉ dẫn. Không gửi production instructions vào câu được đọc.

Nếu có alignment, dùng offset ký tự và trạng thái đang ở trong cặp ngoặc để bỏ cả tag bị tách thành nhiều token. Giữ timestamp gốc của ký tự/lời được giữ lại; không xóa tag rồi zip chuỗi ngắn hơn với mảng timestamps cũ. Không dồn mất thời gian cười/thở vì sẽ làm lệch lời sau đó. Khi đổi tốc độ audio, tạo lại hoặc biến đổi timing nhất quán. Nếu provider không có alignment phù hợp, dùng nhận dạng/forced alignment trên audio cuối với transcript sạch; không bịa timestamp.

## Cấu hình ElevenLabs khi được chọn

Voice ID do người dùng cung cấp: `pNInz6obpgDQGcFmaJgB`; tên yêu cầu Adam. Kiểm tra voice có sẵn trong tài khoản/model trước khi tuyên bố chọn thành công. Model yêu cầu `eleven_v3`; đây là yêu cầu cấu hình, không phải bằng chứng đã gọi API.

Fallback `eleven_multilingual_v2` phải bỏ tags trước khi gửi và ghi rõ mất khả năng diễn xuất bằng tags. Không tự đổi voice/provider khi lỗi. Khóa API chỉ qua cấu hình bảo mật; không ghi giá trị thật vào tài liệu, source hoặc log.

Đã chốt 1.2×. Connector hiện tại không cung cấp trường speed cho V3; áp dụng 1.2× riêng track narration trong CapCut, giữ cao độ, rồi nghe và căn caption theo file sau chỉnh. Không tăng tốc hai lần. Nếu dùng direct API trong tương lai phải xác minh schema trước. Xem [VOICE-POLICY.md](VOICE-POLICY.md) và [bằng chứng connector](audit-20261016-elevenlabs.json).

## Ví dụ cho giá treo hiện tại (chỉ minh họa văn phong)

Raw: `[playful] Mấy dợ nhìn nè... một giá có cả thanh trên, thanh dưới. [excited] Muốn xem đúng mẫu này thì mở giỏ hàng, kiểm tra phân loại nha. Dứt!`

Phụ đề: `Mấy dợ nhìn nè... một giá có cả thanh trên, thanh dưới. Muốn xem đúng mẫu này thì mở giỏ hàng, kiểm tra phân loại nha. Dứt!`

## Tài liệu xác minh

Tra ngày 2026-10-16: [ElevenLabs prompting/best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices), [Speed setting](https://help.elevenlabs.io/hc/en-us/articles/13416271012497-Can-I-slow-down-the-pace-of-the-voice). V3 hỗ trợ audio tags; không khẳng định tính năng chỉ độc quyền V3 ở mọi thời điểm. Hiệu quả từng tag/voice phải nghe thử. Đã tìm thấy đúng Voice ID qua connector; chưa tạo/nghe audio tiếng Việt.

## Công cụ chuẩn bị trong dự án

Dùng `scripts/prepare_adam_voice.py` để tách lời raw/clean từ `creative_plan.json`, kiểm tra chữ số và câu chốt, rồi xuất một payload narration cả video. Có helper lọc character alignment giữ timestamps gốc. Đây là chuẩn bị offline, chưa phải tích hợp API hay render phụ đề CapCut.
