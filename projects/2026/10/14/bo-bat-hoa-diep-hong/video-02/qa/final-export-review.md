# Rà soát hình ảnh cuối — video-02 rebuild

Ngày: 14/10/2026 (Asia/Saigon)

## Phán quyết

**Đạt để so sánh chất lượng hình/voice/caption. Chưa đạt chuẩn xuất bản:** vệt bóng watermark Flow/Gemini vẫn nhận ra ngoài vòng logo, đặc biệt trên nền sáng của cảnh 01. Không chỉnh media trong lượt QA này.

## Artifact và độ ổn định

- File đã rà: `video-02/output/video-02-rebuild.mp4`
- SHA-256 đóng băng đầu lượt và kiểm lại sau lượt rà: `C58F5A55003399E12FCBC3A077956BCE767F97E5922C9DAE4300D5684E6A9C73` (không đổi trong lượt kiểm tra).
- H.264/AAC, 720×1280 (9:16), 24 fps, 327 frame, 13,625 s; audio mono 48 kHz.
- Timeline hình: clip 01 source 0–6,91 s (frame xuất 0–165); clip 03 source 0–2,16 s (frame xuất 166–217); clip 04 source 0–4,375 s, phát ở 0,961538× (frame xuất 218–326). Không có ảnh tĩnh, freeze-frame hoặc end card.

## Phương pháp và giới hạn

- Bản xuất liền trước (SHA `E6466FC2…`) đã được rà đủ 327 frame ở 24 fps. Với revision này, rà lại liên tục toàn vùng thay đổi frame 144–165 (22 frame), vùng liền kề 135–176, cut sau và caption/CTA ở frame 210–233; kiểm lại các frame đầu/cuối và logo. Các đoạn không đổi dùng đúng source clip, overlay và audio asset đã rà ở lượt trước.
- Cut 1 mới: frame 165 (6,875 s, frame bát cuối) → 166 (6,917 s, frame đĩa đầu), timeline khoảng 6,91 s. Cut cũ ở 5,98 s đã được loại.
- Cut 2: frame 217 (9,042 s) → 218 (9,083 s), timeline khoảng 9,07 s.
- Đã thử kiểm tra bề mặt điều khiển để phát liên tục; phiên QA không có browser/player khả dụng (`cua.getState()` trả về không có app/browser). Vì vậy không ghi nhận đã xem video liên tục hoặc nghe trực tiếp bằng tai. Đánh giá audio dưới đây dựa trên so khớp file nguồn, waveform, mức âm và transcript/SRT; không thể xác nhận chủ quan click/tail phụ âm bằng thính giác.

## Hình ảnh, sản phẩm và mạch cảnh

- Đối chiếu `input/product-reference.jpg` và `input/background-reference.jpg`; UI TikTok trong ảnh tham chiếu **không xuất hiện** trong bất kỳ frame xuất nào. Không có UI, nhãn hoặc chữ ngẫu nhiên từ ảnh tham chiếu.
- **Cảnh 01, frame 0–165 (0–6,875 s):** một bát cơm men trắng, viền xám mảnh, họa tiết lá/hoa xám xanh; khớp nhóm sản phẩm trong ảnh tham chiếu. Một tay phải đỡ và nghiêng bát; không thấy ngón thừa/dính, tay phụ, vật thể nhân đôi, hoặc xuyên tiếp xúc. Chuyển động tự nhiên. Nền sáng khác nền tối của hai cảnh sau; thay đổi bối cảnh thấy rõ ở cut.
- **Cảnh 03, frame 166–217 (6,917–9,042 s):** một đĩa men trắng có viền và họa tiết lá/hoa xám xanh đúng nhóm sản phẩm. Một tay phải chạm/đỡ mép đĩa; không có lỗi tay, vật thể dư, hoặc biến dạng trong đoạn đã dùng. Cut vào/ra sạch, không còn cú nhảy scale bị loại ở clip nguồn.
- **Cảnh 04, frame 218–326 (9,083–13,583 s):** một tay phải nhấc và xoay một muỗng/muôi sứ trắng cạnh bộ dụng cụ; dáng men và lỗ treo cán tương ứng món phụ kiện trong ảnh. Không thấy tay phụ, ngón lỗi, hoặc sản phẩm nhân đôi. Cut 9,07 s rõ nhưng không có frame ghost/đen.
- Mạch voice/hình đi từ bát → đĩa → thìa/muôi. Sửa cut đầu giúp cụm “Bộ có bát cơm” (5,96–6,91 s theo phụ đề) nằm trên hình bát đến hết câu; sau cut 6,91 s là hình đĩa, đúng với cụm “nhiều cỡ đĩa” bắt đầu 7,20 s. Cảnh cuối khớp lời tặng thìa/muôi.
- Các frame liền nhau có biến đổi chuyển động sản phẩm/tay/camera; không có khoảng freeze hoặc lặp nguyên frame quan sát thấy.

## Hook, phụ đề và CTA

- Hook “Hoa văn bộ bát này nhìn cận ra sao?” hiện 0–1,5 s ở trên; chữ tương phản đủ và không đè lên bát.
- Phụ đề tiếng Việt có dấu, khớp nội dung transcript đã duyệt và thứ tự câu trong script: mô tả bát → bộ có bát/đĩa → thìa/muôi và CTA. Caption nằm thấp, không che vùng sản phẩm chính. Không thấy ký tự lỗi hoặc chữ sai rõ ở contact sheet.
- CTA “Đối chiếu danh sách món với shop trước khi đặt” hiện 9,15–13,43 s ở trên; tách vùng với phụ đề thoại phía dưới, không che tay/sản phẩm. Các lần đổi chữ/fade không tạo một khoảng trắng dài dễ gây hiểu là phụ đề rơi mất.

## Logo và vệt watermark

- So với `assets/shop-branding.png`: overlay dùng đúng ảnh shop-branding, mặt nạ tròn, ổn định và vẫn nhận ra tên “Mẹo Nhà Gọn Gàng” ở kích thước trình chiếu. Theo `project.json`, vòng hiện tại là 116×116 px tại `(x=557,y=1114)`, tâm `(615,1172)` trên video 720×1280; không drift/flicker, không chạm sản phẩm hoặc phụ đề.
- Watermark nguồn có tâm sao khoảng `(600,1158)`, lệch khỏi tâm logo hiện tại `(+15,+14)` px. Sao chính bị vòng logo che, nhưng bóng nguồn không: ước lượng footprint phần bóng/nhánh ngoài logo khoảng `x≈535–720, y≈1044–1253` (đo thủ công từ crop; sai số vài pixel). Vệt trên/phải và cung tối dưới/trái vẫn lộ ngoài vòng logo.
- **Khoảng frame:** vệt rõ nhất trên nền sáng cảnh 01, frame 0–165 (0–6,875 s), nhìn thấy liên tục; ở frame 166–326 (6,917–13,583 s) vẫn có trace nhưng tương phản thấp hơn trên nền bàn tối. Không thấy dấu sao trắng lộ riêng hoặc overlay bị lệch.
- Căn logo về gần tâm sao sẽ cải thiện độ tâm, nhưng không che các nhánh bóng dài. Một vòng tròn đủ lớn để che gần hết vệt sẽ cần khoảng 210–240 px và quá lớn cho góc; tăng nhẹ đường kính vẫn để lộ bóng. Vì vậy phần dư này là **lỗi release branding**, dù hình/voice/caption dùng được để so sánh.

## Âm thanh và voice

- File trong MP4 khớp rất sát `assets/voiceover-cut.wav` (13,620 s), tức đúng voice asset đã duyệt thay vì TTS: chênh giữa audio AAC giải mã và WAV nguồn có mức trung bình −68,1 dBFS, đỉnh −39,3 dBFS (sai số mã hóa AAC). Audio xuất dài 13,625 s; peak −3,15 dBFS, RMS −18,22 dBFS; không clipping/NaN/Inf.
- Kiểm tra `silencedetect` tại −50 dB trong 80 ms không báo đoạn im lặng bất thường. Waveform và so khớp WAV cho thấy bản dựng giữ đoạn thoại đầu từ 0–5,98 s đúng timeline; transcript/caption khép đủ câu “...họa tiết lá rất thanh nhã” tại 5,98 s. Không có dấu hiệu số học/waveform cho thấy assembler cắt nhầm qua phần voice đã duyệt. Do không nghe trực tiếp, **chưa thể xác nhận chắc chắn bằng thính giác** rằng phụ âm cuối câu đầu hoàn chỉnh hoặc không có click rất ngắn ở mối nối.
- Hai điểm cut hình 6,91 s và 9,07 s không tạo ra ngắt audio giữa câu theo timeline; track narration là một dải liên tục, không có sự kiện silence detection. Chất lượng nghe thực tế vẫn cần lượt nghe player nếu cần chứng nhận click-free tuyệt đối.

## Kết luận QA

- **Đạt vòng so sánh:** hình sản phẩm/tay trong ba cảnh, hai cut, không có still/freeze, không có UI TikTok; nội dung và bố trí hook/caption/CTA; voice asset khớp file nguồn đã duyệt và đúng mạch thoại theo project.
- **Chưa đạt để xuất bản:** bóng watermark nhìn thấy ngoài vòng logo, rõ ở cảnh 01 trên nền sáng. Ghi rõ rằng lượt này chưa nghe video liên tục bằng player.
- File vẫn nguyên hash revision nêu trên; report này không chỉnh file video.
