# TikTok-AI-Editor

Workspace dùng chung để sản xuất và quản lý nhiều video affiliate.

- `.codex/agents/`: vai trò chuyên trách cho script, Flow prompt, post, visual QA, edit và viết caption/hashtag đăng TikTok.
- `.agents/skills/`: workflow video tổng và skill theo ngành hàng.
- `workflow/`: quy trình chung, chuẩn dựng, nghiên cứu xu hướng, caption/hashtag và ví dụ.
- `prompt-origins/`: tài liệu/prompt nguồn bất biến.
- `scripts/`: composer prompt dùng chung.
- `tools/`: công cụ dựng dùng chung. Chạy `python tools/edit_video.py --project projects/2026/10/14/bo-bat-hoa-diep-hong/video-01/project.json` để dựng một video cụ thể.
- `projects/YYYY/MM/DD/<product-slug>/video-NN/`: thư mục riêng cho từng video; xem `projects/README.md`.

Bắt đầu ở `projects/README.md`; đọc `workflow/WORKFLOW.md`, `workflow/TREND-LED-AFFILIATE-PLAYBOOK.md` và `workflow/EDITORIAL-STANDARDS.md` trước mỗi dự án mới.



