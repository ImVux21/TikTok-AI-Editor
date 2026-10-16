# Rà soát hình ảnh và âm thanh — Bộ bát hoa Diệp Hồng

Chuẩn đối chiếu: ảnh sản phẩm `../input/product-reference.jpg`. Ảnh `../input/background-reference.jpg` chỉ để tham chiếu bối cảnh/góc quay; tuyệt đối không sao chép giao diện TikTok. Bản cuối chỉ dùng clip video chuyển động, không có ảnh tĩnh.

| Cảnh | Clip được xét | Phạm vi kiểm tra | Kết quả | Quyết định |
|---|---|---|---|---|
| 01 — Bát cơm | `canh-01-bat-com-thay-the.mp4` | Rà từng khung hình trong 5,23 giây được dùng (126/126 frame ở 24 fps) | Chỉ một tay cầm một bát xuyên suốt; đúng nền sứ trắng, viền xám và họa tiết lá xám; không có UI TikTok hoặc tay phụ | Đạt; thay clip lỗi |
| 02 — Tô hai quai | `canh-02-to-canh-thay-the-4.mp4` | Xem toàn clip và contact sheet đủ 240/240 khung hình ở 24 fps | Chỉ một tay xuất hiện, tô nằm yên trên bàn, hai quai trống; không có tay thừa, tay nền, UI TikTok hoặc biến dạng đáng kể | Đạt; dùng thay cảnh lỗi |
| 03 — Đĩa | `canh-03-dia-su.mp4` | Xem toàn clip; contact sheet 2 fps | Đĩa sứ trắng, họa tiết lá xám; tay giữ/nghiêng có tiếp xúc; không có UI TikTok | Đạt |
| 04 — Thìa | `canh-04-thia-su.mp4` | Xem toàn clip; contact sheet 2 fps | Thìa và muôi sứ trắng; thao tác tay có tiếp xúc; không có UI TikTok. Số lượng quà được nói/chú thích, không suy ra từ clip | Đạt |

## Các bản cảnh tô bị loại

- Clip bát cũ bị loại sau khi rà lại bản xuất vì có nhiều tay cùng xuất hiện quanh bát ở đoạn cận.
- Tạo clip bát thay thế mới trên Flow ngày 14/10/2026: `canh-01-bat-com-thay-the.mp4`. Rà toàn bộ 126/126 frame của đoạn 5,23 giây được đưa vào timeline; chỉ một tay xuất hiện và thao tác tự nhiên. Đoạn dư của clip không được dùng.
- Clip gốc và các lượt thay thế tô đầu tiên bị loại vì có ba hoặc nhiều bàn tay cùng giữ tô.
- `canh-02-to-canh-thay-the-4.mp4` là bản thay thế đạt kiểm tra, tải từ Flow ngày 14/10/2026. Contact sheet được tạo từ 24 fps toàn clip, bao phủ đủ 240 khung hình; một tay phải vào từ phía phải, chạm thành tô rồi rời tay xuống bàn. Không có tay thứ hai, quai luôn trống, tô không bị nhấc.
- Theo yêu cầu của người dùng, không dùng ảnh tĩnh/freeze-frame để che đoạn lỗi. Nếu một cảnh video không đạt thì tạo clip video thay thế và duyệt lại.

## Âm thanh và bản xuất

- Lời đọc được duyệt là MP3 ElevenLabs giọng nữ Chi, `../assets/voiceover.mp3`, thời lượng 20,96 giây. Bản cuối phải dùng chính file này; loại bỏ toàn bộ track TTS nội bộ của CapCut và tắt âm thanh gốc từ các clip Flow.
- Bản xuất cuối `affiliate-video-final-vietnamese.mp4` lấy track lời đọc trực tiếp từ `voiceover.mp3`; âm thanh gốc từ các clip Flow đã bị loại. Lời đọc/đoạn phụ đề được đối chiếu với transcript tiếng Việt của bản thu Chi; không có track TTS nội bộ trong lệnh dựng.
- Bản xuất `../output/final_video.mp4` được nối bốn clip bằng cut thẳng tại các mốc cảnh; bản xuất hiện không áp dụng wipe/dissolve. Contact sheet lịch sử gồm 42 mẫu 2 fps; lưu ý biên bản gốc có ghi transition nhưng lệnh xuất cuối dùng nối clip trực tiếp, nên thông tin này đã được hiệu chỉnh theo bản MP4 được đóng gói.
- Không có ảnh tĩnh/freeze-frame; cảnh tô chỉ một tay; file giữ track thoại ElevenLabs Chi, không có âm thanh gốc từ clip Flow.
- Kiểm tra luồng media: H.264 dọc 720×1280, 24 fps, 503 frame / 20,96 giây; một track AAC 20,96 giây. Bản xuất đạt.

Người dùng cho phép tạo các clip Flow thuộc dự án này qua tài khoản Pro mà không cần hỏi lại về tín dụng. Điều đó không bao gồm mua tín dụng/gói, đổi gói hoặc dịch vụ trả phí ngoài phạm vi.


## Bản xuất có logo shop — sửa ngày 14/10/2026

- Bản badge chữ nhật trước đó quá lớn và không dùng đúng ảnh shop; đã thay thế cùng tên file `output/final_video_logo.mp4` bằng overlay tròn lấy trực tiếp từ `assets/shop-branding.png`.
- Dấu Gemini/Flow là biểu tượng nhỏ quanh tâm (600, 1158), không phải toàn bộ họa tiết lá ở góc. Sau khi so cỡ 64, 92 và 104 px trên cảnh sáng, cảnh đĩa và cảnh cuối có tay, chọn ảnh tròn 92 px để nhận ra logo rõ hơn mà vẫn tách khỏi vùng tay; đặt tại x=554, y=1112, mask lõm 2 px.
- Đã xem frame đầu, giữa, cuối các cảnh và hai phía điểm chuyển tại 4,9 s, 9,8 s, 15,3 s; ảnh tròn ổn định, không thấy biểu tượng lộ ở các frame đã kiểm tra. Phụ đề phía trên không bị che. Cảnh cuối có bàn tay đi gần vùng logo; overlay vẫn giữ đúng tâm watermark.
- Bản xuất vẫn là H.264 dọc 720×1280/24 fps, đủ 503 frame và AAC 20,96 giây như bản gốc. `project.json` lưu nguồn ảnh, kích thước và tọa độ overlay. `output/final_video.mp4` là bản gốc chưa gắn logo.

## Bản xuất phụ đề động — sửa ngày 14/10/2026

- Bản hiện hành: `output/final_video_sub_chay.mp4`. Giữ nguyên cảnh, nhịp cắt, logo shop tròn 92 px và track AAC từ `output/final_video_logo.mp4`.
- Xóa dòng chữ tĩnh đã in vào bản trước ở vùng x=190, y=65, w=340, h=85 bằng FFmpeg delogo, rồi đặt 17 cụm phụ đề động trên cùng vùng hình. Chữ trắng viền tối, từ khóa vàng, hiệu ứng phóng nhẹ và vào/ra ngắn; không che bộ bát.
- Nguồn lời là `assets/voiceover-transcript.srt`; mốc cụm được căn thủ công theo các khoảng ngắt nghe được trong `assets/voiceover.mp3`. File chỉnh sửa: `output/dynamic-captions.ass`; bản phụ đề văn bản: `output/subtitles_dynamic.srt`.
- Đã xem mẫu ở 1,2 giây, 6,8 giây và 16,8 giây trên nền sáng/tối. Bản MP4 là H.264 dọc 720×1280, 24 fps, 503 frame / 20,96 giây và AAC 20,96 giây.
- Tác vụ tự động nhận diện phụ đề của CapCut bị hệ thống duyệt quyền chặn vì cần tải voiceover riêng lên dịch vụ ngoài. Bản này dùng transcript đã duyệt và căn nhịp tại máy, chưa có mốc chính xác từng từ từ công cụ nhận diện.
