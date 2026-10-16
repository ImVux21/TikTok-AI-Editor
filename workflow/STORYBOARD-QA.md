# Cổng QA ảnh storyboard trước Google Flow

Dùng checklist này sau khi tạo **1–3 ảnh storyboard riêng biệt** đã ghép sản phẩm vào đúng phòng, trước khi gửi bất kỳ ảnh nào sang Flow. Mỗi ảnh phải là một khung dọc hoàn chỉnh; không gửi collage nhiều ô. QA ảnh giảm rủi ro sai hình trước khi tạo video nhưng **không chứng minh clip Flow sẽ không phát sinh lỗi chuyển động, hình học hoặc liên tục**. Video vẫn phải qua QA video riêng.

## So sánh và kiểm tra

Mở ảnh storyboard cạnh ảnh sản phẩm gốc và ảnh phòng gốc; đối chiếu từng ảnh và so sánh các ảnh trong bộ với nhau.

- **Sản phẩm:** đúng số lượng, màu, silhouette, tỷ lệ, thanh/khung, móc, chân/đế, mối nối và các chi tiết thấy trong reference. Không thêm/bớt cấu kiện, đổi vật liệu hay làm méo hình.
- **Góc nhìn có căn cứ:** chỉ dùng góc và bề mặt được thấy hoặc suy ra chắc chắn từ ảnh tham chiếu. Không bịa mặt sau, cơ cấu khuất, chi tiết lắp ráp hay cách sử dụng mà ảnh gốc không xác nhận.
- **Phòng:** đúng nhận diện nền, tường/sàn, đường ranh, đồ đạc phải giữ hoặc phải bỏ theo brief. Kiểm tra phối cảnh, tỷ lệ sản phẩm trong phòng, hướng sáng, bóng đổ và điểm tiếp xúc chân sản phẩm với sàn.
- **Tính liên tục:** giữ cùng sản phẩm, phòng, màu, bố cục và phong cách ánh sáng giữa các scene. Nếu có quần áo/đồ vật, kiểm tra số lượng, vị trí, màu và trạng thái nhất quán với kịch bản; không để đồ tự xuất hiện hoặc biến mất nếu cảnh không giải thích điều đó.
- **Bố cục:** kiểm tra khung 9:16, crop đầu/chân/chi tiết, khoảng trống cần cho phụ đề/CTA và vùng an toàn giao diện TikTok. Không để chữ dự kiến che sản phẩm hoặc điểm thao tác.
- **Người và tay (nếu có):** kiểm tra số người/tay, ngón, tư thế, điểm chạm và tương tác có nguyên nhân hợp lý. Không chấp nhận tay thừa/dính/biến dạng hoặc vật thể bị cầm sai cách.
- **Lỗi ảnh:** xem toàn ảnh ở kích thước đầy đủ, sau đó phóng to những vùng quan trọng như móc, mối nối, chân đế, bóng tiếp xúc, bàn tay và ranh sản phẩm/nền. Tìm viền ghép, bóng sai, vật thể ma, chữ/logo bịa, chi tiết lặp hoặc artefact nhỏ.

## Quyết định

Mỗi ảnh phải có một trạng thái riêng: **pending**, **pass**, **fix** hoặc **reject**.

- **Pending:** chưa có đủ reference, chưa kiểm hết các mục, hoặc chưa khóa đúng file/version/hash.
- **Pass:** mọi mục quan trọng khớp reference/brief; không còn lỗi sản phẩm, phòng, người hoặc ghép nền. Chỉ ảnh `pass` mới được phép chuyển sang Flow.
- **Fix:** có thể sửa bằng cách tạo lại ảnh hoặc chỉnh prompt/reference; phiên bản sửa phải được QA lại từ đầu.
- **Reject:** sai nhận diện sản phẩm/phòng, có chi tiết bịa quan trọng, lỗi hình học/anatomy, hoặc không thể sửa đáng tin cậy từ reference hiện có. Không dùng làm khung Flow.

**Phê duyệt gắn với đúng file, version và SHA-256.** Bất kỳ thay đổi nào về ảnh, crop, kích thước, prompt tạo ảnh hoặc nguồn reference đều tạo một version mới và làm mất hiệu lực approval cũ. Ghi trạng thái mới trước khi chuyển sang Flow.

## Mẫu ghi nhận cho từng run

Lưu báo cáo tại `qa/storyboard-review.md` trong thư mục của run. Thêm dòng nếu có nhiều ảnh; không gộp kết quả các scene.

| Scene / file | Version, SHA-256 | Product geometry/count/hooks/base | Room/light/shadow/perspective | Continuity / props | Framing / text safe area | Humans / artifacts at full-size + details | Status | Finding / next action |
|---|---|---|---|---|---|---|---|---|
| scene-01 / `storyboard/scene-01-v01.png` | pending | pending | pending | pending | pending | pending | **pending** | Chưa rà |
| scene-02 / `storyboard/scene-02-v01.png` | pending | pending | pending | pending | pending | pending | **pending** | Chưa rà |
| scene-03 / `storyboard/scene-03-v01.png` | pending | pending | pending | pending | pending | pending | **pending** | Chưa rà |

**Thông tin run:**

- QA bắt đầu/kết thúc (múi giờ): `pending`
- Ảnh sản phẩm gốc / hash: `pending`
- Ảnh phòng gốc / hash: `pending`
- Kịch bản/brief version: `pending`
- Bộ ảnh storyboard được kiểm tra: `pending`
- Quyết định cuối: `pending — chỉ chuyển các file pass sang Flow`

## Ranh giới với QA video

Duyệt ảnh chỉ xác nhận khung tĩnh tại version đã ghi. Nó không thể xác nhận chuyển động, biến dạng giữa frame, tay/ngón xuất hiện thoáng qua, vật thể nhấp nháy, cut, watermark, lời thoại hoặc âm thanh. Khi Flow tạo clip, phải xem trọn clip và rà mọi frame theo quy trình QA video; không suy diễn rằng ảnh ghép tốt sẽ loại bỏ mọi lỗi của AI.
