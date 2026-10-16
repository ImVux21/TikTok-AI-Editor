# Quy trình video affiliate TikTok

Gọi skill `$tiktok-affiliate-video` trong dự án này và gửi tên/link sản phẩm. Chọn [một prompt mẫu cho cả video](PROMPT-MODES.md), sau đó skill điều phối các agent theo các phụ thuộc dưới đây. Các việc độc lập chạy song song theo [quy tắc điều phối](../AGENTS.md).

## Giọng đọc — quyết định mới 2026-10-16

Người dùng đã chọn ElevenLabs V3 (Adam) cho narration và CapCut để ghép. Áp dụng [VOICE-POLICY.md](VOICE-POLICY.md) và [ADAM_V3_PROMPT_SPEC.md](ADAM_V3_PROMPT_SPEC.md). Flow chỉ tạo hình/ambience từ storyboard, không sinh thoại. Ưu tiên một track narration toàn video, tách raw có tags khỏi phụ đề sạch, căn cut theo audio thực tế đã duyệt. Quyết định này thay các mặc định Flow speech cũ.

## Đầu vào storyboard — cập nhật 2026-10-16

Luồng mặc định: **brief và kịch bản tổng → tạo 1–3 ảnh ghép sản phẩm vào phòng → duyệt ảnh → prompt chuyển động → Flow → duyệt clip → tạo và nghe narration ElevenLabs V3 → CapCut → duyệt bản xuất**. Có thể chuẩn bị narration song song với Flow sau khi script đã khóa; cut/caption cuối chốt theo audio đã nghe. Ưu tiên giải quyết lỗi hình ngay ở ảnh đầu vào. Đây là biện pháp giảm rủi ro làm lại, chưa phải kết luận rằng hai ảnh rời là nguyên nhân duy nhất hay ảnh ghép sẽ loại bỏ lỗi chuyển động.

- Agent script chọn số ảnh và góc có giá trị cho nội dung, tối đa 3 ảnh riêng khung dọc 9:16. Không đưa một collage nhiều ô vào Flow. Chốt bố cục một ảnh tổng trước, rồi dùng ảnh đó cùng ảnh sản phẩm gốc để giữ thiết kế/phòng nhất quán khi tạo các ảnh còn lại. Chỉ chọn góc có căn cứ trong ảnh gốc; tránh tự dựng mặt sau hoặc cấu tạo bị khuất.
- Coordinator điều phối công cụ tạo ảnh với ảnh sản phẩm và ảnh phòng làm reference. Mỗi ảnh phải là cảnh hoàn chỉnh: đúng sản phẩm, đúng nền, tỷ lệ/phối cảnh hợp lý, ánh sáng và bóng tiếp xúc thống nhất; bỏ chiếc kệ cũ theo brief. Lưu vào `storyboard/scene-01-v01.png` …, cùng prompt và danh sách reference. Ảnh ghép là staging, không phải chứng cứ trải nghiệm hoặc tính năng sản phẩm.
- QA duyệt từng ảnh và tính liên tục cả bộ theo [STORYBOARD-QA.md](STORYBOARD-QA.md); lưu quyết định tại `qa/storyboard-review.md`. Coordinator ghi file, SHA-256, scene, version và đường dẫn báo cáo trong `project.json`. Chỉ ảnh có kết quả **pass** được chuyển sang Flow. Ảnh thay đổi phải duyệt lại; approval phiên bản cũ không chuyển sang ảnh mới.
- Flow nhận ảnh storyboard đã duyệt cho đúng cảnh làm khung đầu; không yêu cầu Flow ghép lại hai ảnh sản phẩm/phòng gốc. Không mặc định ép cùng một ảnh ở cả đầu/cuối khi hành động làm trạng thái cảnh thay đổi. Nếu cần khung cuối, tạo và duyệt đúng trạng thái cuối trước. Kiểm tra UI/model hỗ trợ chế độ ảnh thành video ở thời điểm chạy; screenshot cũ chỉ là tham khảo.
- Prompt Flow mới chỉ định chuyển động, camera, điều gì phải giữ nguyên, không thoại/người nói và nối cảnh. Lời thoại/tags nằm trong đầu vào V3 riêng. Dùng [STORYBOARD-FLOW-PROMPT.md](STORYBOARD-FLOW-PROMPT.md) để xử lý xung đột với mẫu gốc; giữ nguồn mẫu nguyên vẹn và ghi override storyboard/audio. Không để lệnh ghép ảnh/đổi phòng từ mẫu cũ phủ định frame đã duyệt.
- Dùng [STORYBOARD-SCRIPT.md](STORYBOARD-SCRIPT.md) để nối hook, phần cho thấy đặc điểm và CTA. Chuẩn bị cảnh tiếp khi QA video cảnh trước chạy; một cảnh Flow đại diện phải đạt trước khi tiếp tục cùng kỹ thuật. Ảnh storyboard không thay thế video bị lỗi trong bản xuất. Giọng/tốc độ theo [VOICE-POLICY.md](VOICE-POLICY.md).

Khởi điểm biên tập cho sản phẩm đơn giản: 18–24 giây (ví dụ 3 đoạn khoảng 7 giây), sau đó cắt theo lời thoại thực tế. Không kéo dài cảnh chỉ để đủ thời lượng. TikTok có hướng dẫn 21–34 giây cho nhiều quảng cáo và nhấn mạnh hook sớm; không coi số đó là tối ưu chung cho mọi video affiliate organic. Nguồn tra ngày 2026-10-16: [TikTok video advertising guide](https://ads.tiktok.com/business/en/guides/video-advertising-guide), [Creative best practices](https://ads.tiktok.com/business/en/blog/creative-best-practices-top-performing-ads). Đo lại thời gian tạo ảnh, image QA, Flow, video QA và dựng để đánh giá thay đổi này có giảm tổng thời gian hay không.

## Chạy song song

Cấu hình dự án bật subagent và đặt tối đa 3 luồng subagent, ngoài agent điều phối. Agent điều phối giữ tab Flow; QA nhận từng clip ngay khi tải xong. Trong lúc Flow tạo cảnh tiếp, QA rà cảnh đã tải và agent hậu kỳ chuẩn bị nhịp lời đọc/phụ đề. Chỉ ghép clip đã được QA duyệt. Chuyển quyền draft CapCut từ assembler sang editor bằng một bàn giao rõ ràng; không cùng sửa draft. Agent bài đăng có thể tra nguồn trước nhưng chỉ viết gói cuối cho đúng bản xuất đã đạt QA.

Thử và duyệt một cảnh đại diện trước khi tạo hàng loạt theo cùng cách. Nếu cùng lỗi sản phẩm xuất hiện hai lần, xem lại ảnh tham chiếu và cách quay trước khi tạo thêm. Ghi thời gian từng giai đoạn và số lần thử để phát hiện chỗ chờ lâu.

## Rút ngắn thời gian làm một video

Mục tiêu là giảm vòng lặp và thời gian chờ thủ công; thời gian render Flow vẫn phụ thuộc dịch vụ. Trước khi mở Flow, hoàn tất preflight trong `project.json`: ảnh storyboard đã pass QA, variation/claim nào chưa xác minh, hook và lời đọc, hành động chính, framing, đầu ra dự kiến. Prompt cảnh chỉ bắt đầu sau khi script và storyboard đã khóa. Chọn một chuyển động rõ, ít đạo cụ và ít thay đổi trạng thái; khung cuối chỉ dùng khi phù hợp hành động và đã được duyệt.

Mỗi thiết kế cảnh có tối đa hai lượt tạo thông thường. Sau lần QA đầu, ghi đúng lỗi quan sát được và đổi nguyên nhân gốc (reference, action hoặc camera) nếu lỗi đó tái diễn; không tiêu lượt thứ ba cho các chỉnh prompt nhỏ. Chỉ cho phép lượt tiếp theo sau thay đổi thiết kế có ý nghĩa và ghi lý do vào attempt log. Không giảm QA: clip được tải xuống chuyển sang full review ngay, chỉ dùng các range được QA duyệt, và export cuối vẫn phải qua review toàn khung.

Giới hạn thời gian chờ download ở mỗi lần kiểm tra; khi quá giới hạn, kiểm tra trạng thái và đổi đường tải hoặc codec/container thay vì lặp lại cùng thao tác. Chuẩn bị EDL, caption timing và assets trong lúc clip đang được QA. Tái sử dụng track narration đã duyệt khi chỉ sửa hình/caption; không sinh lại audio/video cho thay đổi hậu kỳ. Ghi giờ bắt đầu/kết thúc từng phase và thời gian Flow/download riêng để biết phần nào có thể tối ưu nội bộ.

`project.json` là nguồn chuẩn cho trạng thái vận hành, attempt log, EDL, asset và export. `video-profile.json` giữ brief/reference/template/script provenance và trỏ tới trạng thái hiện tại trong project; không để hai file mang các trạng thái chờ khác nhau. Trước khi chạy renderer, xác nhận manifest đọc được và toàn bộ asset tồn tại; dùng `tools/edit_video.py --project <project.json>` với manifest timeline hiện hành. Thời gian ước tính nội bộ không bao gồm render/download Flow và không phải cam kết thời lượng.

| Bước | Agent | Đầu vào | Đầu ra / điều kiện chuyển bước |
|---|---|---|---|
| 1. Research ngành hàng và kịch bản tổng | `affiliate_script` | Link sản phẩm, ảnh sản phẩm, thị trường đăng | Tra hướng dẫn/trend hiện hành theo thị trường và ngành hàng; ghi nguồn, ngày tra, tín hiệu sáng tạo; khóa một mẫu trong `video-profile.json`; viết kịch bản dọc có hook, hành động quay được, bằng chứng và CTA |
| 2a. Tạo và duyệt storyboard | Coordinator + `affiliate_visual_qa` | Script, ảnh sản phẩm/phòng gốc | 1–3 ảnh ghép riêng 9:16, QA từng ảnh và cả bộ; lưu version/hash/report; ảnh pass mới được animate |
| 2b. Prompt từng cảnh | `affiliate_flow_prompt` | Script, storyboard đã pass, hồ sơ mẫu | Prefix animate đúng frame, continuity và không thoại; **cùng một prompt mẫu gốc** với override đã ghi; thời lượng theo scene và model thực tế |
| 3. Tạo clip Flow | Codex điều phối | Prompt và storyboard đã duyệt của cảnh | Clip theo cấu hình đã xem trên Flow. Với người dùng này, đã có quyền thường trực dùng tín dụng Flow trong phạm vi dự án từ tài khoản Pro; không hỏi lại giá/tín dụng cho các lượt tạo cảnh thuộc dự án. Quyền này không bao gồm mua tín dụng/gói, đổi gói, hoặc dịch vụ trả phí ngoài phạm vi dự án. |
| 4. Kiểm tra hình | `affiliate_visual_qa` | Clip Flow, ảnh sản phẩm, ảnh nền | Xem hết từng clip, rà contact sheet tối thiểu 2 fps; kiểm tra từng frame ở đoạn có tay/chuyển động hoặc nghi lỗi. Ghi phạm vi rà, file và mốc lỗi; **đạt / tạo clip thay thế hoặc cắt clip video đã đạt rồi duyệt lại / loại clip**. Không duyệt chỉ từ vài keyframe; ảnh tĩnh không thay thế clip video bị lỗi. |
| 5. Dựng bản nháp và giọng | `affiliate_post` | Chỉ clip đã đạt, kịch bản lời đọc | Dùng track ElevenLabs V3 Adam đã duyệt theo lựa chọn mới; giữ raw tags riêng khỏi phụ đề, căn theo audio cuối; loại thoại Flow để không chồng giọng. Dựng trình tự, lời đọc và phụ đề; chuyển bản nháp cho editor chuyên nghiệp. |
| 6. Biên tập chuyên nghiệp | `pro_video_editor` | Bản nháp, toàn bộ nguồn đã duyệt, lời đọc và brief | Tối ưu nhịp kể, điểm cắt, liên tục hình ảnh, chuyển cảnh vừa đủ, nhạc/voice/caption. Dùng CapCut atomic transition workflow khi draft hỗ trợ; preview thay đổi rồi lưu/xuất bản kiểm tra. Không chèn ảnh tĩnh thay cảnh video lỗi. |
| 7. Duyệt bản cuối | `affiliate_visual_qa` | Bản xuất cuối và asset nguồn | Xem hết video, kiểm tra mọi frame quanh chuyển cảnh, xác nhận đúng nguồn giọng, phụ đề khớp, không còn tay/sản phẩm lỗi, không có ảnh tĩnh. Ghi coverage, mốc và quyết định đạt/không đạt. |
| 8. Chuẩn bị bài đăng | `affiliate_publishing` | **Đúng MP4 cuối đã đạt QA**, transcript, listing/claim đã xác nhận, thị trường đăng | Nghiên cứu caption/hashtag cùng ngành gần ngày xuất; lưu nguồn/ngày và mức xác minh; viết caption chính + phương án B, hashtag liên quan, CTA đúng giỏ hàng vào `publishing/post-package.md`. Chạy lại khi bản xuất hoặc thông tin bán hàng đổi; không tự đăng. |

## Hồ sơ cần cho mỗi sản phẩm

- Ảnh sản phẩm: ít nhất một ảnh rõ, tốt nhất nhiều góc. Ảnh này quyết định hình dáng và màu sắc đúng.
- Ảnh nền trống: dùng nhất quán cho các cảnh. Ảnh logo shop là tài sản riêng, không thay thế ảnh nền.
- Link sản phẩm hoặc thông tin bán hàng đã xác nhận: dùng để kiểm tra tính năng, kích thước, giá và lời quảng bá.
- Lựa chọn giọng: ElevenLabs V3, Adam theo voice ID đã chỉ định; xác minh voice trong tài khoản và nghe toàn track. Tốc độ 1.2× đã chốt; áp dụng riêng audio trong CapCut theo khả năng connector hiện tại. Xem [quy tắc giọng đọc](VOICE-POLICY.md).

## Logo shop và watermark Flow/Gemini

Trong QA nguồn, ghi nhận vị trí và kích thước thật của watermark Gemini/Flow trên từng cảnh. Dùng đúng ảnh shop người dùng đã cung cấp (`workflow/assets/shop-branding.png` hoặc bản sao trong dự án), mask ảnh thành hình tròn và đặt tâm trùng watermark. Thử vài cỡ trên khung 9:16 ở kích thước điện thoại; chọn cỡ đủ nhận ra logo và che kín biểu tượng, đồng thời không lấn vào sản phẩm, tay, phụ đề, CTA hoặc giao diện TikTok. Tránh badge chữ tự dựng, mảng chữ nhật và ảnh vuông chiếm cả góc. Giữ logo ổn định suốt thời gian watermark xuất hiện, điều chỉnh theo cảnh nếu dấu đổi vị trí. Rà frame đầu/cuối, giữa cảnh và hai phía của mọi chuyển cảnh. Lưu nguồn logo, kích thước và tọa độ overlay trong `project.json` để bản dựng lại vẫn có logo.
## Mặc định Flow đang dùng

[Ảnh cấu hình Flow đã lưu](assets/flow-config-reference.png) cho thấy: **Video · Thành phần · 9:16 · Omni 1.1 Flash · 720p · 10 giây · x1**. Giá hiển thị là 15 tín dụng cho cấu hình tại thời điểm chụp. Kiểm tra lại giao diện và giá trước mỗi lần tạo vì chúng có thể đổi.

## Chuẩn biên tập chuyên nghiệp

Xem [tiêu chuẩn dựng video ngắn](EDITORIAL-STANDARDS.md), [playbook nghiên cứu theo ngành](TREND-LED-AFFILIATE-PLAYBOOK.md) và agent `pro_video_editor`. Ưu tiên clean cut, cut theo hành động, match cut theo hình/động tác và sound bridge. Chỉ dùng dissolve/fade khi hợp ngữ cảnh; không gắn wipe cố định để làm clip có vẻ “mượt”. Nếu shot pair yếu, đổi thứ tự/chọn shot/cắt lại. Luôn preview ở tốc độ bình thường và rà từng frame vùng chuyển cảnh.

## Ví dụ hiện tại: kẹp xanh dương

Có một hồ sơ mẫu tham khảo trong [examples/kep-xanh-duong/video-profile.json](examples/kep-xanh-duong/video-profile.json). Đây chỉ là ví dụ chọn prompt; chưa đủ ảnh nền và link sản phẩm để sản xuất. [Ảnh “Mẹo Nhà Gọn Gàng”](assets/shop-branding.png) là ảnh thương hiệu shop, không phải background trống hoặc logo trong suốt.




## Caption và hashtag khi xuất video

Xem [playbook caption/hashtag](POST-CAPTION-HASHTAG-PLAYBOOK.md). Sau khi bản cuối đạt QA, luôn giao cho `affiliate_publishing` tạo gói nội dung của đúng bản xuất. Nếu không xem được số liệu trend hiện hành, ghi rõ và dùng hashtag mô tả sản phẩm/ngữ cảnh; không hứa viral.

