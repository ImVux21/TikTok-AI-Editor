# QA video 03 — 2026-10-14

## Trạng thái
**REJECT — chưa xuất bản dựng.** Chưa có tệp MP4 1080×1920 cuối.

## Cảnh đã rà
Đã tạo contact sheet ở 24 fps cho toàn bộ 8 giây (192 khung/cảnh) của các clip nguồn cục bộ; riêng clip tạo từ ảnh gốc người dùng được xem trực tiếp trong Flow (chưa tải về nên chưa qua kiểm tra toàn bộ 192 khung).

| Cảnh | Kết quả | Lỗi thấy trong khung hình |
|---|---|---|
| 01 — `clip-01-source-720p.mp4` | Reject | Bàn tay xuất hiện dù prompt cấm người; miếng lót biến dạng/phóng phủ khung; bộ bàn ăn xuất hiện qua nội suy không tự nhiên. |
| 02 — `clip-02-source-720p.mp4` (bản cũ trong dự án 03) | Reject | Ban đầu lặp lại bàn trống rồi chuyển sang mâm ăn; không giữ đúng chức năng cảnh cận họa tiết. |
| 02 — `clip-02-replacement-720p.mp4` | Reject | Đĩa hoa văn phóng cực lớn chồng lên mâm, che phần lớn bữa ăn. |
| 02 — `Camera filming table at home` (Veo 3.1 Quality, tạo lại) | Reject | Dù prompt cấm người/bàn tay, hai tay bưng đĩa xuất hiện ở khoảng 00:02; sai hành động và thiết kế khung hình. |
| 03 — `clip-03-source-720p.mp4` | Reject | Điện thoại xuất hiện thành vật thể ở giữa bàn và chiếm khung trước khi hình ảnh chuyển vào màn hình điện thoại. |
| 02 — `Family meal video prompt` (dùng ảnh gốc) | Reject tạm thời | Xem trước cho thấy máy quay lao vào đĩa rau, không nhấn hoa văn bát đĩa; khung dọc còn viền đen vì ảnh nguồn vuông. Chưa tải/soát toàn bộ khung. |

## Bản thoại
Giọng Chi đã được tạo theo xác nhận 554 tín dụng và lưu ở `input/voice-chi-approved.mp3`. Kiểm tra lại: file dài 42,31 giây. Kết luận trước đây về 17,3 giây im lặng cuối là sai; silencedetect không xác nhận khoảng lặng đó. Node ElevenLabs completed nhưng đầu vào trộn hướng dẫn tiếng Anh với lời thoại Việt. Chưa duyệt nội dung audio; không cắt tại 24,65 giây vì chưa xác định điểm kết thúc lời đọc. Cần nghe/đối chiếu đầy đủ trước khi dùng.

## So sánh với video 02
Video 02 là bản 720p dùng Omni 1.1 Flash với ba cảnh đã qua QA hình ảnh. Cảnh Veo 3.1 Quality của video 03 có độ biến động camera rõ hơn, nhưng vẫn làm sai hình học/hành động của sản phẩm trong các cảnh đã kiểm tra; vì vậy chưa có cơ sở để chấm bản mới tốt hơn. Đây không phải so sánh kiểm soát vì nội dung cảnh và cách dựng khác nhau.

## Tiếp theo
Cần video thật ngắn quay bộ bát trên bàn ăn (8–12 giây, camera lia chậm, không cần lời nói) để giữ đúng dáng sản phẩm và tránh cảnh AI tự sinh tay/đĩa/điện thoại. Sau khi có footage nguồn đạt QA mới dựng voice, phụ đề, nhãn tái hiện AI và bản 1080×1920.


Lượt Veo 3.1 Quality cuối dùng chính ảnh bàn ăn người dùng gửi làm hai khung mốc, nhưng vẫn không bám được chi tiết sản phẩm. Tổng hiện tại: 6 lần tạo Flow x 100 tín dụng = 600 tín dụng theo báo giá giao diện, cộng 554 tín dụng cho giọng Chi đã được duyệt.
