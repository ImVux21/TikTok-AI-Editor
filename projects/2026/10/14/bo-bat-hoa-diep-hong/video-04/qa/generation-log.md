# Nhật ký tạo — video 04

Ngày: 2026-10-14 (Asia/Saigon)

| Giai đoạn | Bắt đầu | Kết thúc | Kết quả / thời lượng |
|---|---|---|---|
| Chuẩn bị project và kiểm tra cài đặt Flow | 16:25 | 16:32 | Dự án Flow video-04 được tạo; Veo 3.1 Lite, Frames, 9:16, 720p, 8 giây, x1. Báo giá giao diện: 10 tín dụng. |
| Tạo clip | 16:35:56 | 16:37 | Flow tạo xong clip 8 giây; asset `a161165d-ea15-4a98-8dfb-b118b4108d0e`. Thời gian tạo khoảng 64 giây. |
| Tải clip | 16:37 | 16:40 | Flow hiện thông báo đang tải bản 720p nhưng không tìm thấy MP4 trong Downloads hoặc Temp. Trình duyệt từ chối mở trang quản lý download theo chính sách. Chưa có tệp cục bộ. |
| QA nguồn hình/tiếng | Chưa bắt đầu | Chờ | Bị chặn: chưa có tệp để nghe toàn bộ clip hoặc kiểm tra sản phẩm từng khung. |
| Draft và xuất CapCut | Chưa bắt đầu | Chờ | Bị chặn chờ clip đã qua QA nguồn. |

## Kiểm tra UI và audio

- Flow project: `https://flow.google.com/project/28eab504-fb48-4091-aec4-5236d64628ab`
- UI hiện `Video · 720p · 8 giây`, khung hình dọc 9:16 và model `Veo 3.1 - Lite`; chế độ output `x1`.
- Bộ cài đặt không hiển thị bộ chọn giọng Adam hay công tắc audio riêng. Veo 3.1 Lite hỗ trợ audio tạo cùng video theo [model card chính thức của Google DeepMind](https://deepmind.google/models/model-cards/veo-3-1-lite/); lời thoại vẫn phải được nghe và xác minh trên clip thực tế.
- Tín dụng báo giá trước khi tạo: 10. Đã gửi một lần tạo; đây là báo giá giao diện, không phải xác nhận số tín dụng thực tế bị trừ.
- Tham chiếu đã chọn từ thư viện project video 03, không tải tệp cục bộ lên: `table-after-ai.png` dùng làm khung đầu và cuối.
- Flow hiển thị clip mới dài 8 giây trong project, nhưng thao tác tải xuống chưa tạo được tệp tìm thấy trong các thư mục dự kiến. Không thể nghe hoặc duyệt hình qua bằng chứng này; chưa đánh dấu QA đạt.
- Chưa tạo draft CapCut và chưa xuất video do quy trình yêu cầu clip nguồn được duyệt trước khi dựng.
- Adam không có bộ chọn hiển thị; phong cách nam trầm, rõ và tự nhiên đã được mô tả trong prompt. Không xác minh được preset Adam.
- Tệp prompt đầy đủ: `../prompts/scene-01.full.txt`. Tệp tham chiếu, mã lần tạo và project được lưu trong `../project.json`.

