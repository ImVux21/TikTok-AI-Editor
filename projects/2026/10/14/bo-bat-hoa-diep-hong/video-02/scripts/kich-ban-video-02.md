# Kịch bản dựng lại — Video 02

**Mục tiêu:** Bản so sánh mới dùng ba clip chuyển động QA chấp thuận (cảnh 01, 03, 04) và voiceover ElevenLabs Chi hiện có đã rút gọn. Kể thành một lượt “xem cận hoa văn rồi kiểm tra những phần đi kèm”: bắt đầu bằng bát, qua đĩa, rồi chốt bằng phụ kiện và hướng người xem kiểm tra danh sách món.

**Thời lượng / khung:** mục tiêu khoảng 13,62 giây, dọc 9:16, 720×1280, 24 fps. Dựng video-only, không ảnh tĩnh, freeze-frame hay end card. Chỉ dùng cảnh 01, 03, 04. Loại toàn bộ ứng viên cảnh 02 theo QA; không thay bằng ảnh, freeze frame hoặc clip khác. Template nguồn trong profile giữ nguyên HANDHELD; không tạo Flow clip mới.

**Hook hình ảnh 0–1,5 giây:** Mở ngay lúc bàn tay đang nghiêng bát để lộ hoa văn. Chữ mở: **“Hoa văn bộ bát này nhìn cận ra sao?”** Đặt trong vùng an toàn trên cùng, không che sản phẩm. Không intro/logo mở đầu. Giữ voiceover đã rút gọn bắt đầu từ frame đầu.

| Thời gian | Hình / máy quay / tiếng | Lời đọc đã duyệt | Chữ hiển thị | Cơ sở / dựng |
|---|---|---|---|---|
| 0–6,91s | `canh-01-bat-com-thay-the.mp4`, source 0–6,91s. Cận bát cơm trong tay; giữ chuyển động nghiêng/kiểm tra hoa văn. Hook phủ 0–1,5s; phụ đề ở vùng thấp đồng bộ lời. Tắt audio Flow. | “Nhìn cận bộ bát hoa Diệp Hồng này nhé: nền sứ trắng, viền xám và họa tiết lá rất thanh nhã.” Câu kế tiếp bắt đầu ở 5,98s; cụm “Bộ có bát cơm” tiếp tục trên cảnh bát đến cut 6,91s. | Hook đầu; phụ đề chính xác theo lời. | Giữ hết cụm “Bộ có bát cơm” tới 6,91s trên hình bát; lời thoại tiếp tục liền qua cut. |
| 6,91–9,07s | `canh-03-dia-su.mp4`, source 0–2,16s. Cận đĩa được tay giữ/nghiêng để thấy mép và hoa văn. Tắt audio Flow. | Từ 6,91s, phần còn lại của câu là “nhiều cỡ đĩa để bày mâm cơm gọn, đẹp.” “Bộ có bát cơm” đã chạy trên cảnh bát 5,98–6,91s. Câu này ghép từ phần lời gốc trước/sau cụm bị lược; không thu thêm lời. | Phụ đề động khớp câu đã ghép; không hiện tổng số món. | Loại câu về tô canh và cụm “và tô canh” (13,50–14,25s). Clip đĩa dùng từ đầu, dừng an toàn trước cú nhảy scale tại 4,42s nguồn. |
| 9,07–13,62s | `canh-04-thia-su.mp4`, source 0–4,375s ở tốc độ 0,9615× (kéo chậm 4% để giữ trọn cảnh trước cú nhảy scale). Cận thìa và muôi; tắt audio Flow. | “Tặng kèm 10 thìa sứ trắng và một muôi canh. Xem chi tiết bộ bát ở giỏ hàng nhé.” | Phụ đề động theo lời; CTA ở vùng an toàn phía trên, kết thúc trước điểm nhảy scale. | Câu quà bắt đầu xấp xỉ điểm cắt sang cảnh này. Tổng số món vẫn chưa được shop xác nhận; không dùng ảnh tĩnh/freeze-frame. |

## Âm thanh và phụ đề

- Giữ nguyên file nguồn `../assets/voiceover.mp3` (giọng Chi, 20,96s) và tạo track dựng bằng cách giữ 0,00–6,91s + 11,35–13,50s + 14,25–15,23s + 16,15–20,70s. Bỏ câu về tô canh, cụm “và tô canh” và khoảng lặng trước câu quà; hard cut sau câu mở để giữ trọn âm cuối và crossfade tối đa 20ms tại hai mối nối phía sau. Track thành phẩm khoảng 13,62s. Không tạo/thu TTS mới.
- Tắt âm thanh gốc của cả ba clip. Không cần nhạc mới; ưu tiên lời đọc rõ và không thêm tiếng đặt bát giả vì clip không cung cấp cảnh/âm thanh đó.
- Dùng phụ đề động ngắn theo cụm lời, căn với transcript hiện có; nhấn ít từ khóa, giữ đủ thời gian đọc và không che bát/hoa văn/tay. Hook chỉ xuất hiện lúc 0–1,5s, sau đó nhường chỗ cho phụ đề.
- Dùng cut thẳng tại 6,91s và 9,07s; không thêm wipe/dissolve. Giữ ảnh shop-branding tròn ở vị trí che watermark theo project.json; không dùng làm end card.

## Giới hạn hình ảnh và claim

- Chỉ ba clip chuyển động 01, 03, 04 được QA chấp thuận; mọi ứng viên cảnh 02 bị loại vì không có bản dùng được. Không có cảnh mâm cơm/bàn ăn rộng hoặc cảnh ăn/uống. Không lời thoại hay chữ nào được ám chỉ creator đã nấu, dùng bữa, tự nhận xét cảm giác cầm/nặng/độ bền, hoặc kiểm tra thực tế ngoài những gì hình ảnh cho thấy.
- Không nêu tổng số 30 hay 31: tên listing ghi 30, phần mô tả ghi 31, còn danh sách thành phần cộng 30 (19 món chính + 11 món tặng). Cần shop xác nhận món thứ 31 trước khi dùng con số tổng.
- Không nêu giá, kích thước ngoài những gì clip/listing đã xác nhận, chất liệu “cao cấp”, chịu nhiệt, độ bền, chính sách bù vỡ hoặc các claim công năng chưa xác minh.
- Footage chuyển động AI đã qua rà soát hình, không phải bằng chứng trải nghiệm người dùng. Lời đọc vì thế chỉ mô tả hình dáng/hoa văn và thông tin listing đã có.

## Vì sao câu chuyện này hợp video và thị trường

Với clip được chấp thuận, góc “xem cận hoa văn rồi các món đi kèm trước khi quyết định” trả lời được câu hỏi mua hàng bằng sản phẩm đang chuyển động. Nhịp đi từ bát có hoa văn → đĩa → thìa/muôi. Cảnh tô bị lược vì QA không chấp thuận ứng viên nào, nên không thay bằng hình giả, ảnh hay một template khác. Hướng này bám tín hiệu TikTok Next 2026 về tò mò và “Emotional ROI” cùng hướng dẫn TikTok Shop Việt Nam về hook sớm, giá trị thông tin và chữ hỗ trợ xem khi tắt tiếng. Đây là lựa chọn dựa trên hướng dẫn nền tảng, không phải tuyên bố format đang thịnh hành hoặc sẽ tăng chuyển đổi.

## Câu hỏi còn ảnh hưởng đến nội dung

Shop cần xác nhận danh sách chính xác gồm món thứ 31 là gì, hoặc sửa tên/mô tả cho thống nhất. Đến khi nhận được xác nhận, giữ CTA yêu cầu người xem đối chiếu danh sách và không đọc tổng số.



