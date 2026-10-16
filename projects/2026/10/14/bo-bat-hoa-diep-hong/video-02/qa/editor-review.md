# Rà soát biên tập bản dựng lại — video-02

Ngày: 14/10/2026 (Asia/Saigon)

## Artifact được rà

- `output/video-02-rebuild.mp4` — H.264/AAC, 720×1280, 9:16, 24 fps, 13,625 giây, 327 frame; 48 kHz mono. SHA-256: `C58F5A55003399E12FCBC3A077956BCE767F97E5922C9DAE4300D5684E6A9C73`.
- Cấu hình xuất từ `project.json`; chỉ gồm clip 01 (0–6,91 s), clip 03 (0–2,16 s) và clip 04 (nguồn 0–4,375 s, tốc độ 0,9615× / 4,55 s). Không có nhạc, ảnh tĩnh, freeze-frame, TTS hay âm thanh gốc của Flow.

## Quyết định và kết quả biên tập

- Giữ nhịp kể bát cơm → đĩa → thìa/muôi. Hai điểm đổi cảnh là cut thẳng tại 6,91 s (bát→đĩa) và 9,07 s (đĩa→thìa/muôi), không hiệu ứng trang trí. Cụm lời “Bộ có bát cơm” được giữ trên hình bát đến hết 6,91 s; “nhiều cỡ đĩa” bắt đầu trên hình đĩa. Rà sát các frame quanh cả hai điểm cắt: không thấy frame ghost, lặp sản phẩm hoặc gián đoạn hình ngoài thay đổi bối cảnh có chủ đích.
- Hook ở 0–1,5 s và phụ đề bám lời Chi. Chữ CTA hướng dẫn đối chiếu danh sách ở phía trên; phụ đề lời đọc ở vùng thấp. Cả hai vùng cách sản phẩm và không chạm vùng điều khiển TikTok.
- Đối chiếu phụ đề với transcript đã duyệt và các đoạn nguồn được giữ. Chỉ giữ giọng ElevenLabs Chi đã duyệt; file dựng dùng `assets/voiceover-cut.wav`. Độ dài âm thanh 13,62 s khớp độ dài timeline. Không phát hiện đoạn im lặng dài theo ngưỡng −50 dB/80 ms; peak −3,15 dBFS, RMS −18,22 dBFS, không clipping.
- So sánh vòng che shop ở 104, 116 và 128 px trên ảnh điện thoại/crop góc. Chọn vòng 116 px tại x=557, y=1114 để che dấu sao Gemini/Flow đã đo và tăng che vùng bóng mà vẫn chừa khoảng trống ở góc. Dùng đúng `assets/shop-branding.png`, mặt nạ tròn; không che bát/đĩa, tay hoặc phụ đề. Vệt bóng đổ rộng hơn dấu sao vẫn còn một phần ở ngoài vòng; không phóng vòng thêm vì sẽ làm nhãn hiệu lớn và sát mép dưới hơn mức cần thiết.
- Đã xuất lại qua `tools/edit_video.py`. Không thay đổi clip nguồn, lời thoại, nội dung phụ đề, tổng độ dài hay branding; điểm cắt đầu chuyển từ 5,98 s sang 6,91 s, điểm cắt thứ hai giữ ở 9,07 s.

## Phạm vi QA

Xem contact sheet bản xuất ở bước 0,5 giây, kiểm tra các frame liền kề quanh hai cut, rà bố cục chữ/logo và metadata xuất. Rà audio bằng độ dài, silence detection và astats; kiểm tra phụ đề theo transcript, không ghi nhận là đã nghe toàn bộ audio bằng trình phát. QA nguồn frame-by-frame được ghi riêng ở `source-clip-review.md`.



