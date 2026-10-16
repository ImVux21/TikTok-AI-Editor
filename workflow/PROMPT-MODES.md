# Chọn một prompt mẫu cho cả video

Một video đăng TikTok có **một prompt mẫu gốc duy nhất**. Chọn mẫu theo nhóm sản phẩm **và cách kể chuyện mong muốn** trước khi tạo clip, rồi lưu tên tệp và SHA-256 trong `video-profile.json`. Mọi cảnh tạo bằng Flow trong video đó dùng lại chính mẫu này; chỉ phần mở đầu mô tả hành động của cảnh thay đổi.

| Nhóm | Skill chuyên trách | Các nguồn nguyên văn đã lưu | Cách chọn một mẫu |
|---|---|---|---|
| Đồ gia dụng | `$affiliate-homegoods` | [DAILY VLOG](assets/daily-vlog-mode.txt), [HANDHELD](assets/handheld-product-review.txt) | Chọn **một**: video sinh hoạt có thao tác/kết quả được kiểm chứng → DAILY VLOG; video cho xem sản phẩm trong tay → HANDHELD |
| Thay đồ thang máy | `$affiliate-fashion-elevator` | [Toàn bộ mục gốc](assets/fashion-elevator-source.txt) | Chọn đúng đoạn mẫu cho video thử/trưng bày trang phục; mục này chứa nhiều prompt riêng, nên cần xác định đoạn nào là mẫu trước khi khóa |
| Sức khỏe | `$affiliate-health` | [Toàn bộ mục gốc](assets/health-source.txt) | Chọn bản có thoại hoặc không thoại cho cả video; xác minh các tuyên bố sức khỏe trước khi dùng |

[Bản Word gốc không thay đổi](assets/Affiliate-original.docx) được lưu để đối chiếu. Các bản `.txt` từ Word giữ nguyên nội dung chữ theo thứ tự đoạn; việc chuyển định dạng Word thành văn bản có thể đổi kiểu chữ và ngắt đoạn. Riêng HANDHELD được sao chép đúng từng byte từ tệp người dùng dán, và nội dung trùng mục trong Word sau khi chuẩn hóa khoảng trắng.

**Không đưa cả mục “Thay đồ thang máy” hoặc “Sức khỏe” vào Flow như một prompt duy nhất**: mỗi mục chứa nhiều chỉ dẫn/prompt khác nhau. Chọn đúng đoạn gốc, sao chép nguyên chữ vào tệp mẫu đã khóa, rồi mới tạo các phần mở đầu cho từng cảnh. Không viết lại prompt gốc.

## Kẹp xanh dương đang làm

[Hồ sơ video](examples/kep-xanh-duong/video-profile.json) đã khóa **HANDHELD PRODUCT REVIEW MODE** vì người dùng chọn `[prompt:handheld]` và hiện có ảnh chỉ đủ để đối chiếu ngoại hình chiếc kẹp. Các clip Flow của video này đều dùng HANDHELD. Cảnh mở đầu hoặc kết thúc không phù hợp với HANDHELD sẽ dùng ảnh/video thật và dựng trong CapCut, hoặc kịch bản được sửa để cảnh vẫn là cầm xem sản phẩm. Không chuyển một cảnh sang DAILY VLOG trong cùng video.

## Khi dùng storyboard đã ghép (2026-10-16)

Giữ nguyên tài liệu nguồn và hash mẫu khóa. Theo yêu cầu mới của người dùng, prefix có override rõ ràng: animate ảnh storyboard đã pass QA, không ghép lại ảnh sản phẩm/phòng, không tự đổi đạo cụ hoặc hình dáng để thực hiện chỉ dẫn mâu thuẫn trong mẫu gốc. Cùng một override áp dụng nhất quán toàn video và lưu trong profile; kiểm tra prompt hoàn chỉnh trước khi gửi. Xem [hướng dẫn prompt storyboard](STORYBOARD-FLOW-PROMPT.md). Bộ ảnh được duyệt quyết định bố cục, script quyết định hành động và lời; không mặc định template có quyền thay đổi chúng.

## Quy tắc âm thanh cho mọi mẫu

Người dùng đã chọn ElevenLabs V3 Adam + CapCut ngày 2026-10-16; theo [VOICE-POLICY.md](VOICE-POLICY.md). Flow chỉ tạo hình/ambience, không thoại. Ghi override này trong hồ sơ và prompt cuối nếu mẫu gốc yêu cầu thoại. Audio tags chỉ gửi V3, không gửi Flow hay phụ đề. Giữ nguyên nguồn mẫu; không sửa audio/provenance của bản xuất cũ.
