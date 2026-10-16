# Thư viện dự án TikTok-AI-Editor

## Quy ước lưu trữ

Mỗi video nằm theo đường dẫn `projects/YYYY/MM/DD/<product-slug>/video-NN/`. Ngày là ngày bắt đầu sản xuất; slug dùng chữ thường không dấu và dấu gạch ngang. Tạo `video-01`, `video-02` khi cùng sản phẩm/ngày có concept hoặc video độc lập. Các lần sửa của cùng video được ghi trong `video-NN/qa/` và xuất thành phiên bản riêng trong thư mục output.

```text
projects/
  YYYY/
    MM/
      DD/
        product-slug/
          video-01/
            input/
            assets/
            prompts/
            scripts/
            output/
            qa/
            publishing/
            project.json
```

Sau mỗi bản xuất đạt QA, lưu gói nội dung đăng TikTok trong `publishing/post-package.md` và ghi đường dẫn trong `project.json`. Không trộn tài nguyên giữa video hoặc ngày. Nếu dùng lại một tài sản, copy vào video mới hoặc ghi rõ nguồn tương đối. Prompt gốc dùng chung nằm trong `prompt-origins/` và được giữ nguyên.

## Nội dung hiện có

- `2026/10/14/bo-bat-hoa-diep-hong/video-01/`: bản dựng cũ và kịch bản quay cập nhật. Muốn dựng theo kịch bản mới cần footage bàn ăn thật.

## Tạo video mới

Sao chép thư mục `projects/_template/video-01/` vào thư mục ngày/sản phẩm mới. Đặt ID tiếp theo (`video-01`, `video-02`...), cập nhật `project.json`, rồi lưu mọi tệp của video trong các thư mục con tương ứng. Không dùng lại thư mục output của video khác.

