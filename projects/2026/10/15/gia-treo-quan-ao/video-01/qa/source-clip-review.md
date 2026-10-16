# QA nguồn — giá treo quần áo, video-01

## Trạng thái

**REJECT — không bàn giao dựng.** Clip không giữ đúng background photo đã chỉ định: toàn bộ phòng dựng thành một góc tường trắng trơn có đèn downlight, góc tường/baseboard và sàn gỗ sáng khác. Đây là sai lệch nhìn thấy xuyên các cảnh, không thể sửa bằng chèn ảnh hoặc freeze frame; cần clip video mới được review lại.

## Thông tin clip đã review

- File chính xác: output/scene-01-flow-attempt-01.mp4
- Flow project ID: 0ce18ce1-20cf-4d75-9e07-c1ab4987f615
- Generated asset/editor ID: f642a966-d7f5-4664-b51b-b3115d3d7e5a
- Attempt: 1; model Omni 1.1 Flash; Video Components; 9:16; 720p; 10 giây; x1; cấu hình được báo 15 credits.
- ffprobe: H.264 720×1280, 24/1 fps, 240 frame, thời lượng video đúng 10.000 s; AAC stereo 48 kHz, thời lượng audio 10.005 s.
- Nguồn đối chiếu chính xác: input/product-photo-2.jpg, input/background-photo-1.jpg; script scripts/script.md; prompt prompts/scene-01-flow-prompt.txt.

## Độ phủ và giới hạn review

- Đã giải mã và kiểm tra contact sheet phủ **240/240 frame ở 24 fps**, theo thứ tự frame, gồm 10 sheet chia theo từng giây: qa/contact-sheets/second-00.png đến second-09.png. Các khoảng có tay được xem thêm ở ảnh chi tiết qa/hands-detail/.
- Không có frame trùng liên tiếp; bộ lọc phát hiện gần-trùng giữ 232/240 frame ở ngưỡng đã thử, không thấy đoạn freeze tĩnh. Tuy nhiên môi trường subagent này không có bề mặt phát video/audio tương tác. Vì vậy **chưa thể xác nhận đã xem liên tục clip ở tốc độ bình thường hoặc nghe trực tiếp toàn bộ thoại**. Kết luận dưới đây dựa trên giải mã/frame review; âm thanh được ghi rõ là chưa xác minh, không suy ra đúng từ prompt.

## Findings

| Thời gian | Hạng mục / bằng chứng | Mức độ | Quyết định |
|---|---|---|---|
| 00:00–00:10 | Background mismatch xuyên clip: ảnh nền chuẩn là phòng có mảng tường hai tông với ranh sơn gồ ghề, sàn ván gỗ mật ong và không gian phẳng một mặt. Clip lại có góc phòng tường trắng trơn, trần/đèn downlight, chân tường, góc tường và sàn vân gỗ sáng khác; bố cục và ánh sáng cũng đổi. Kệ/shelf cũ đã bị bỏ đi, nhưng không giữ căn phòng được cung cấp. | Nghiêm trọng | **Reject; tạo clip video mới và QA lại.** |
| 00:00–00:01.2 (xấp xỉ; các frame thấy tay ở hands-detail/at-00_0.png đến at-01_0.png) | Một bàn tay/forearm trái cầm một móc áo nhẹ và đưa lên thanh; không thấy bàn tay thứ hai, tay nhân đôi, tay nổi hay chi tiết ngón dị dạng trong 24-fps contact scan; các ngón nhìn thấy có vẻ hợp lý. | Không phát hiện lỗi | Pass hạng mục tay trong các frame quan sát; cần playback trực tiếp nếu cần xác nhận tiếp xúc ở tốc độ thường. |
| 00:03.5–00:04.8 (xấp xỉ; hands-detail/at-03_5.png đến at-04_5.png) | Một bàn tay cầm móc/áo, đưa áo lên thanh trước. Không thấy tay thừa hoặc lỗi giải phẫu rõ ràng; ngón bị khuất một phần bởi móc và cổ áo trong một số frame, không thể đếm riêng từng ngón ở mọi frame bị che. | Không phát hiện lỗi | Pass hạng mục tay trong các frame thấy được; tiếp xúc trông hợp lý nhưng cần playback trực tiếp để xác nhận chuyển động. |
| Toàn clip | Sản phẩm màu đen; các shot rộng thể hiện hai khung/ray đặt lệch tầng, giằng ngang, móc hông và chân cong, nhìn chung phù hợp hình sản phẩm. Không thấy kệ gỗ/giày cũ hay logo được bịa. Có vài cảnh cận cắt mất một phần cấu trúc theo ý đồ; shot toàn cuối có đủ sản phẩm. | Không thấy sai nhận diện rõ | Pass nhận diện sơ bộ theo frame scan; chưa xác nhận bằng playback liên tục. |
| 00:00–00:10 | Watermark Flow/Gemini là dấu sparkle trắng ở góc phải dưới, xuất hiện xuyên clip. Ước lượng trên frame 8.0s: bbox x≈576–630, y≈1138–1183 px (54×45 px), tâm x≈603,y≈1160; không đổi vị trí đáng kể trong sheet. | Ghi nhận | Không reject vì watermark. Bản dựng cuối phải mask logo đúng nguồn theo workflow và kiểm tra lại. |
| 00:00–00:10 | Embedded AAC audio tồn tại, nhưng không thể nghe trong runtime review này; câu thoại thực tế, ngôn ngữ, số lần, độ rõ, biến đổi giọng và đồng bộ caption đều **chưa xác minh**. Adam selector chưa được reviewer này quan sát; prompt chỉ yêu cầu phong cách Adam. | Chưa xác minh | Chưa đạt audio gate; coordinator cần nghe toàn bộ trong Flow player trước dựng. Không khẳng định đã chọn preset Adam. |

## Disposition

Clip nguồn output/scene-01-flow-attempt-01.mp4 **không được chuyển sang CapCut** do sai background reference. Không che đoạn lỗi bằng still/freeze/photo. Nếu có clip thay thế, bàn giao đường dẫn file và generation ID chính xác để review lại. Contact sheets và ảnh crop watermark giữ trong qa/ làm hồ sơ lần review này.

## Mốc pha QA

- Chuẩn bị QA bắt đầu: ghi ở lần tạo ghi chú ban đầu.
- Handoff clip từ coordinator: 2026-10-15, sau thông báo Flow asset f642a966-d7f5-4664-b51b-b3115d3d7e5a.
- Hoàn tất frame scan/ghi kết luận: 2026-10-15 10:21:27 +07:00.
- Giới hạn còn mở: continuous playback và nghe audio chưa thực hiện được trong runtime QA subagent.
# Run timeline — video-01

## 2026-10-15 production continuation

- 10:39:10 +07:00 — Attempt 03 submitted in Google Flow after staging `input/background-replaced-rack.png` with the intended rack. Prompt uses the locked 10-second daily-vlog template and reference order: replacement plate first, product image second. Model Omni 1.1 Flash; 9:16, 720p, 10 sec, x1; displayed estimate 15 credits.
- 10:39:12 +07:00 — Flow showed generation progress at 0%; subsequent poll showed 5%. Rendering remains in progress. Generation ID and download name are not yet visible in this run's project metadata.
- The earlier attempt 01 QA ended 10:21:27 +07:00 and rejected the room mismatch after checking 240/240 frames. Audio playback, spoken words, and exact Adam preset remain unverified.
- Attempt 02 is referenced in prior chat notes as another smooth-wall result, but its exact generation ID, downloaded filename, and completed full QA report were not recovered in this continuation. Do not attribute an unverified ID/file to attempt 02.
- Open requirements: finish attempt 03 generation, capture exact generation ID/model/refs/download file and time, hand the exact downloaded clip to full visual QA, listen to the source speech and confirm words/voice against policy, then proceed only with QA-passed material. Final export and publishing package remain pending.

- Attempt 02 record reconciled at 10:45 +07:00 from saved prompt and Flow history: prompt saved as prompts/scene-01-attempt-02-flow-prompt.txt, reference order believed to be background photo first then product photo. No exact generation ID or downloaded file was recovered, so the reported smooth-wall result remains a visual impression only and was not presented as a full QA pass.

- Attempt 03 full visual QA completed 10:48 +07:00; **reject/hold**. Exact report: qa/source-clip-attempt03-review.md, full scan 240/240 frames. Defects: old plant visible in opening then disappears, approximately 8–10 garments on one rail, final 0.3 s cuts to cropped garment close-up. Main room match/product identity pass. AAC exists; reviewer could not listen; actual speech and Adam preset unverified. No clip handed to editing.
