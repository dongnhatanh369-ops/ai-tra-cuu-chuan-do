# PROGRESS - AI Tra Cứu Chuẩn Độ

## Trạng thái hiện tại

- Repository: `ai-tra-cuu-chuan-do`
- Nhánh chính: `main`
- Nhánh phát triển frontend: `feature/frontend-phase1`
- Trạng thái: Đang phát triển nền tảng AI backend

## Đã hoàn thành

### Giai đoạn 0 - Khởi tạo dự án

- [x] Tạo repository và cấu hình nhánh `main`.
- [x] Tạo cấu trúc thư mục backend, frontend, tài liệu và dữ liệu.
- [x] Chọn Python/FastAPI làm nền tảng backend.
- [x] Tạo `pyproject.toml`.
- [x] Tạo `.env.example` và `.gitignore`.
- [x] Tạo API health check tại `GET /health`.
- [x] Viết hướng dẫn phát triển tại `docs/DEVELOPMENT.md`.
- [x] Cập nhật roadmap theo hướng phát triển AI backend trước.

### Frontend thử nghiệm - Nhánh riêng

- [x] Tạo giao diện chat AI thử nghiệm.
- [x] Tạo ô nhập câu hỏi tiếng Việt.
- [x] Hiển thị câu hỏi người dùng và câu trả lời AI.
- [x] Hiển thị trạng thái đang xử lý và lỗi kết nối.
- [x] Cấu hình gọi API `POST /api/v1/ai/chat`.
- [x] Đẩy lên nhánh `feature/frontend-phase1`.
- [ ] Chưa tích hợp vào website chính.
- [ ] Chưa hoạt động hoàn chỉnh vì backend AI chưa có endpoint tương ứng.

## Đang thực hiện

- [x] Giai đoạn 2: bộ tính toán chuẩn độ cơ bản trên nhánh `feature/titration-calculator`.
- [ ] Thiết kế API backend cho hỏi đáp AI.
- [ ] Xây dựng system prompt chuyên về chuẩn độ.
- [ ] Kết nối mô hình AI.
- [ ] Phân loại câu hỏi tra cứu, tính toán, quy trình và an toàn.

## Chưa thực hiện

- [ ] Bộ tính toán chuẩn độ xác định.
- [ ] Tra cứu tài liệu bằng RAG.
- [ ] Quản lý và nạp tài liệu PDF/DOCX/TXT.
- [ ] Kết nối frontend với backend thật.
- [ ] Tích hợp vào website hiện tại.
- [ ] Kiểm thử end-to-end.
- [ ] Triển khai production.

## Lịch sử thay đổi chính

| Commit | Nội dung |
|---|---|
| `b576f4c` | Khởi tạo cấu trúc dự án Giai đoạn 0 |
| `9994441` | Cập nhật roadmap, ưu tiên AI backend |
| `b9a6157` | Tạo frontend thử nghiệm trên nhánh riêng |
| `a710c8b` | Loại frontend thử nghiệm khỏi `main` |

## Ghi chú

- `main` chỉ giữ nền tảng và tài liệu chính của dự án.
- Các tính năng mới nên phát triển trên nhánh riêng rồi mới tạo Pull Request.
- Không lưu API key thật trong repository.
