# Kịch bản test video-02 — giá treo quần áo

**Phạm vi:** Kịch bản + bố cục storyboard cho cùng sản phẩm ở video-01; chỉ mô tả reveal trực quan của giá treo trống. Không tự tạo lời chứng thực, trình diễn lắp ráp, thử tải, hoặc thêm quần áo/đạo cụ chưa được thống nhất. Bối cảnh là staging tạo sinh: thay kệ cũ trong ảnh phòng bằng sản phẩm ảnh tham chiếu.

## Lời đọc và phụ đề

**Một track ElevenLabs V3 (raw, audio tags chỉ dùng trong TTS):**

`[curious] Mấy dợ... một cái giá, hai thanh treo á?! [playful] Nhìn nè, thanh trên, thanh dưới... bên hông còn có móc nữa! [playful] Mấy ní nhớ chọn đúng phân loại trong giỏ nha. Dứt lẹ!`

**Caption sạch, không có tags:**

`Mấy dợ... một cái giá, hai thanh treo á?! Nhìn nè, thanh trên, thanh dưới... bên hông còn có móc nữa! Mấy ní nhớ chọn đúng phân loại trong giỏ nha. Dứt lẹ!`

Lời đọc không có chữ số. Không thêm thông tin giá, kích thước, tải trọng, giảm giá hay trải nghiệm cá nhân. Dùng giọng Adam theo spec người dùng cung cấp sau khi xác minh voice có thể chọn; không nói đã chọn hoặc render thành công trước khi kiểm tra. Tạo một track narration cho toàn video; đặt speed 1.2x đúng một lần trong CapCut, giữ cao độ, nghe lại toàn track rồi mới căn caption theo audio cuối.

## Ba beat hình ảnh và storyboard đề xuất

**Độ dài dựng:** để thời lượng thực của narration V3 và footage đã QA quyết định; khoảng 18–24 giây chỉ là điểm bắt đầu biên tập nếu audio/nhịp hình đủ, không kéo shot để lấp thời gian. Mỗi beat có thể dùng một scene video riêng trong giới hạn model, rồi cắt theo audio.

| Beat | Mục đích | Hình ảnh/động tác | Lời đọc tương ứng | Chữ trên khung |
|---|---|---|---|---|
| Một — hook/reveal | Tạo tò mò bằng sự đối chiếu ngắn “một giá / hai thanh”, đồng thời cho thấy cấu trúc ngay đầu. | Khung master 3/4 rộng, toàn bộ giá và cả hai thanh nằm trong hình ngay từ frame đầu. Chỉ push-in nhẹ; không mở bằng crop sát để Flow phải tự dựng lại hình học. Giá vẫn trống. | “Mấy dợ... một cái giá, hai thanh treo á?!” | “Một giá • hai thanh” |
| Hai — chi tiết/payoff | Cho thấy chính xác các bộ phận nhìn thấy. | Một khung medium/detail đã pre-compose, giữ được cả hai thanh và móc bên trong cùng bố cục. Chỉ một chuyển động máy nhỏ để lia từ hai thanh tới móc; không đổi sản phẩm, phòng hoặc ánh sáng. Không thêm tay, áo, túi hay phụ kiện. | “Nhìn nè, thanh trên, thanh dưới... bên hông còn có móc nữa!” | “Thanh trên • thanh dưới” rồi “Móc bên hông” |
| Ba — CTA | Kết lại bằng toàn sản phẩm và hướng xem đúng biến thể. | Trở về cùng master 3/4 với cùng góc phòng và sản phẩm trống; một settle nhẹ, giữ video chuyển động tới hết. | “Mấy ní nhớ chọn đúng phân loại trong giỏ nha. Dứt lẹ!” | “Chọn đúng phân loại trong giỏ” |

Storyboard: tối đa ba ảnh **riêng biệt, đủ khung dọc 9:16**, mỗi ảnh là một beat trên; không ghép thành collage. Soi đúng silhouette hai thanh, móc bên, chân/giằng và bối cảnh. Chỉ rõ đây là staging tạo sinh. Storyboard ảnh chưa được QA/duyệt trong file này; tham chiếu vị trí đầu ra dự kiến `storyboard/`.

## Template hình ảnh — chưa khóa

- `DAILY VLOG MODE` là mẫu gần nhất vì bối cảnh là góc nhà, nhưng mẫu yêu cầu cảm giác vlog đời thường có thao tác/use action. Run này chỉ cho reveal giá trống, không có hành động sử dụng đã xác minh nên chưa khớp đầy đủ.
- `HANDHELD PRODUCT REVIEW MODE` không phù hợp vì đây là giá treo đứng sàn, không thể cầm trên tay để review.
- Khuyến nghị an toàn: giữ câu chuyện reveal thuần thị giác như trên, **chưa khóa hoặc gửi prompt Flow** cho tới khi coordinator xác nhận ngoại lệ/template phù hợp. Không bịa thêm động tác chỉ để khớp mẫu.

## Ranh giới dữ kiện và continuity

- Ảnh sản phẩm cho thấy khung đứng màu đen, hai thanh treo ở hai mức, móc bên và kết cấu chân/đỡ phía dưới. Kịch bản chỉ nêu hai thanh và móc bên.
- Listing có nhiều phân loại; variation chính xác tương ứng ảnh chưa xác minh. CTA yêu cầu người xem kiểm tra đúng phân loại.
- Không khẳng định chất liệu/sơn của đúng variation, số đo, giá, số lượng trong bộ, tải trọng, độ chắc/bền, khả năng chứa giày, lắp dễ hay tiết kiệm diện tích.
- Không dựng mặt sau/khớp nối/kệ/phụ kiện không có trong tham chiếu. Giữ giá trống và cùng một bố cục trong cả ba frame/scene; không có vật thể xuất hiện hoặc biến mất.
- Chỉ dựng/export sau khi storyboard pass QA; chỉ dùng clip video đã được visual QA duyệt. Đọc toàn bộ audio cuối và rà caption sau khi speed 1.2x đã áp dụng.

