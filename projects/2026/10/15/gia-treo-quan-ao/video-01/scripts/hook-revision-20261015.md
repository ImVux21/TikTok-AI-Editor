# Hook revision — giá treo hai thanh

**Ngày nghiên cứu:** 15/10/2026. **Thị trường:** TikTok Shop Việt Nam. **Trạng thái:** kịch bản đề xuất; chưa phải lời/audio đã tạo hoặc clip đã qua QA. Giữ một mẫu nguồn `10-SECOND DAILY VLOG MODE` đã khóa trong `video-profile.json`; một đoạn Flow 10 giây là một scene. Không dùng ảnh tĩnh để thế cảnh video.

## Quyết định sáng tạo

Người xem đang thiếu chỗ treo và muốn nhìn thấy giá này khác gì một thanh treo thông thường. Mở thẳng bằng móc áo đang chuẩn bị treo, rồi chuyển góc để **hai thanh ngang ở hai độ sâu cùng hiện rõ**. Lời dẫn chỉ vào điều nhìn thấy; CTA dẫn người xem kiểm tra đúng mẫu hai thanh trong giỏ. Cách này đưa lý do cân nhắc mua hàng vào câu chuyện, thay cho câu cảm thán chung chung.

**Hook chọn — 0–3 giây:** “Khoan, giá này có *hai* thanh treo à? Nhìn phía sau nè.”

**Hook B để thử nếu tạo bản khác:** “Treo áo kín một thanh rồi? Mẫu này còn một thanh phía sau nữa.” Chỉ dùng khi hình ngay 0–3 giây thực sự cho thấy cả hai thanh; câu đầu là tình huống khán giả, không phải lời chứng thực của người làm video.

## Lời thoại 10 giây đề xuất

> “Khoan, giá này có hai thanh treo à? Nhìn phía sau nè. Một khung, hai thanh để chia đồ dễ nhìn hơn. Cần thêm chỗ treo? Mở giỏ xem đúng mẫu hai thanh nhé.”

Giọng nam Việt thấp, rõ, ngạc nhiên nhẹ ở “hai”, sau đó như chỉ cho một người bạn xem; không lên giọng rao hàng. “Adam” là phong cách người dùng yêu cầu, **preset cụ thể chưa xác minh trong Flow**. Tốc độ cần thử trong clip 10 giây; nếu quá gấp, bỏ “dễ nhìn hơn” trước khi tạo. Lời này cần Flow tạo mới và phải nghe duyệt toàn bộ. Không ghép lời mới lên clip cũ rồi nhận là audio Flow được duyệt.

## Storyboard và nhịp dựng

| Mốc | Hình và camera | Âm thanh/lời | Chữ trên màn hình | Căn cứ |
|---|---|---|---|---|
| 0.0–0.7s | Frame đầu có bàn tay đưa một móc áo tới gần thanh trước; cắt vào chuyển động, không có logo intro. Giữ tay/sản phẩm rõ trong vùng an toàn. | Tiếng móc chạm nhẹ nếu âm thực sạch; bắt đầu “Khoan…” ngay frame đầu. | “Ủa, 2 thanh treo?” | Ảnh sản phẩm và các clip cho thấy hai thanh; cần QA bàn tay từng frame. |
| 0.7–2.8s | Cut trên chuyển động móc áo sang góc 3/4 hoặc toàn cảnh, giữ cả thanh trước và thanh sau trong cùng khung. Chừa đủ 0.8s để mắt kịp đọc hai thanh. | “…giá này có **hai** thanh treo à? Nhìn phía sau nè.” Nhấn “hai”; SFX nhỏ đúng điểm lộ thanh sau, không dùng whoosh át lời. | “Thanh trước / thanh sau” đặt gần hai thanh, tránh che sản phẩm. | Cấu trúc hai thanh nhìn thấy trong `input/product-photo-2.jpg`; không hàm ý thử tải. |
| 2.8–6.9s | Toàn cảnh chuyển động rất nhẹ trong căn phòng đã thay kệ; hai thanh luôn phân biệt rõ. Nếu có hành động treo, tối đa một móc/áo nhẹ cho mỗi điểm, hình thực tế phải đúng geometry và QA đủ frame. | “Một khung, hai thanh để chia đồ dễ nhìn hơn.” Nhạc nền tiết chế. | “Chia đồ theo 2 thanh” | Lợi ích sử dụng được suy ra trực tiếp từ cấu trúc hai thanh; chưa chứng minh số áo tối đa. |
| 6.9–10.0s | Giữ trọn giá, hai chân, hai thanh và móc bên trong khung; vẫn là video chuyển động. Cut trước khi méo cảnh hoặc cuối clip bị lỗi. | “Cần thêm chỗ treo? Mở giỏ xem đúng mẫu hai thanh nhé.” | “Xem đúng mẫu 2 thanh trong giỏ” | Listing có nhiều phân loại; chưa khóa đúng biến thể theo ảnh. |

Chữ cần biên tập sau khi nghe lời thực tế, không cho Flow tự sinh chữ. Tránh che watermark bằng chữ; xử lý watermark theo quy trình của dự án. Không dùng SFX được dựng giả như bằng chứng về độ chắc chắn.

## Ba file người dùng chọn: khả năng dùng lại

- `Filming_daily_vlog_product_scene_20261015101525.mp4` = attempt 01. Góc cận tay/móc, góc lộ hai thanh, móc bên hông, sau đó nhiều áo. **QA cũ bác vì phòng sai cả clip**; không lấy nguyên clip hoặc mở đầu từ đây khi yêu cầu giữ phòng ảnh nền.
- `Filming_daily_vlog_product_scene_20261015104150.mp4` = attempt 03. Có cận tay/móc ở đầu và toàn cảnh giá trên sàn gỗ với tường hai màu. QA cũ ghi cây lọt 0–1.1s, lỗi số lượng áo và cuối 9.7–10s. Góc hai thanh ở khoảng 1–3s là ứng viên **chỉ sau khi QA mới duyệt chính xác in/out**; chưa được đánh dấu PASS.
- `Filming_daily_vlog_product_scene_20261015105751.mp4` = attempt 04. Có cận tay/móc ở đầu và toàn cảnh thấy cả hai thanh trên nền tường hai màu. QA cũ ghi lỗi nhiều áo từ khoảng 4s và cuối 9.7–10s. Góc rộng khoảng 1–3s là ứng viên **chỉ sau khi QA mới duyệt chính xác in/out**; chưa được đánh dấu PASS.

Các nhận xét hình trên dựa vào contact sheet 1 fps, không phải rà toàn bộ frame. QA phải xác minh cắt đầu, cây/đồ ngoài ảnh, hình dạng khung, bàn tay, âm thanh và điểm cắt của mọi đoạn trước khi dựng. Không dùng cả ba clip như ba cảnh hoàn chỉnh chỉ vì trông ổn khi xem nhanh. Nếu không có đoạn đủ sạch, cần một scene video mới cùng mẫu nguồn. Clip mới cần giữ đúng phòng gốc, nhịp hook và lời thoại ở trên; không thêm tuyên bố lắp đặt/trải nghiệm cá nhân.

## Claim và tư liệu còn thiếu

Ảnh sản phẩm xác nhận khung đen đứng, hai thanh ngang và móc bên. Chưa xác nhận kích thước, tải trọng, độ bền, vật liệu chính xác, giá/ưu đãi, lắp dễ, số áo treo được hay biến thể đang chọn. Trang [PDP người dùng gửi](https://shop.tiktok.com/vn/pdp/1732793679097070628) không đọc được trực tiếp qua web trong lượt này; giữ CTA “đúng mẫu hai thanh” để tránh dẫn nhầm phân loại. Cảnh phòng là dàn dựng bằng Flow, không kể như người dùng đã mua/lắp/thử thật.

## Nguồn nền tảng và cách áp dụng

- [TikTok Shop VN, “Tăng Cường Hiệu Quả Bán Hàng Với Video Chất Lượng Cao”](https://seller-vn.tiktok.com/university/essay?knowledge_id=7335143716456209&lang=vi-VN), đăng 28/07/2026, xem 15/10/2026: nhấn mạnh hình/âm rõ, giá trị thông tin và kịch bản thu hút. Vì vậy hook cần đọc được hai thanh ngay trong 3 giây, thoại gắn với hình.
- [TikTok Creative Center, “Creative Tips for Home and Lifestyle”](https://ads.tiktok.com/business/creativecenter/quicktok/online/creative-tips-for-home-and-lifestyle/pc/en), xem 15/10/2026: gợi ý hook liên quan tình huống người xem, sản phẩm trong ngữ cảnh nhà, thông điệp và CTA; hướng dẫn không phải bằng chứng một format đang trend ở Việt Nam. Vì vậy chọn câu hỏi “hai thanh treo?” và reveal ngay bằng camera.
- [TikTok for Business, “Video Advertising Guide for Small Businesses”](https://ads.tiktok.com/business/en/guides/video-advertising-guide), xem 15/10/2026: khuyến nghị giá trị trong ba giây đầu và phụ đề dễ đọc. Vì vậy không mở bằng phòng trống/chữ logo; đưa móc áo, hai thanh và caption ngắn lên ngay.

Không có số liệu Creative Center hay Search Insights hiện hành chứng minh hook này đang thịnh hành. Đây là phương án phù hợp sản phẩm và các cảnh có sẵn, cần thử bản dựng thực tế.
