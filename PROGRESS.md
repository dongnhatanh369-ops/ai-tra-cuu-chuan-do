# PROGRESS - AI Tra Cứu Chuẩn Độ

## Trạng thái hiện tại

- Repository: `ai-tra-cuu-chuan-do`
- Nhánh chính: `main`
- Nhánh tích hợp: `feature/integrated-ai`
- Trạng thái: Đang phát triển nền tảng AI backend

## Đã hoàn thành

### Giai đoạn 0 - Khởi tạo dự án

- [x] Tạo repository và nhánh `main`.
- [x] Tạo cấu trúc backend, frontend, tài liệu và dữ liệu.
- [x] Chọn Python/FastAPI làm nền tảng backend.
- [x] Tạo cấu hình dự án, `.env.example` và `.gitignore`.
- [x] Tạo API health check tại `GET /health`.
- [x] Viết hướng dẫn phát triển.

### Frontend thử nghiệm

- [x] Tạo giao diện chat AI thử nghiệm.
- [x] Tạo ô nhập câu hỏi tiếng Việt.
- [x] Hiển thị câu hỏi, câu trả lời, trạng thái xử lý và lỗi kết nối.
- [x] Chuẩn bị gọi API `POST /api/v1/ai/chat`.
- [x] Tối ưu responsive cho điện thoại, máy tính bảng và desktop.
- [x] Tối ưu vùng nhập liệu và nút bấm cho màn hình cảm ứng.
- [x] Hỗ trợ safe area trên thiết bị có tai thỏ.
- [x] Hỗ trợ màn hình dọc và ngang.
- [x] Đã chạy thử giao diện tại cổng local `5504`.
- [ ] Chưa tích hợp vào website chính.
- [ ] Chưa hoạt động hoàn chỉnh vì backend AI chưa có endpoint tương ứng.

### Giai đoạn 2 - Bộ tính toán chuẩn độ

- [x] Module tính số mol, nồng độ và thể tích.
- [x] Hỗ trợ hệ số phương trình phản ứng.
- [x] Hỗ trợ đơn vị mL/L.
- [x] API tính toán `POST /api/v1/titration/calculate`.

### Giai đoạn 3 - Tra cứu tài liệu bước đầu

- [x] Nạp tài liệu Markdown/TXT.
- [x] Chia tài liệu thành các đoạn nhỏ.
- [x] Tìm kiếm đoạn liên quan theo từ khóa.
- [x] API tra cứu `POST /api/v1/documents/search`.

## Đang thực hiện

- [ ] Thiết kế API backend hỏi đáp AI.
- [ ] Xây dựng system prompt chuyên về chuẩn độ.
- [ ] Kết nối mô hình AI.
- [ ] Phân loại câu hỏi tra cứu, tính toán, quy trình và an toàn.
- [ ] Bổ sung embedding và vector database cho RAG.

## Chưa thực hiện

- [ ] Đọc tài liệu PDF/DOCX.
- [ ] Gửi ngữ cảnh tài liệu cho mô hình AI.
- [ ] Kết nối frontend với backend thật.
- [ ] Tích hợp vào website hiện tại.
- [ ] Kiểm thử end-to-end.
- [ ] Triển khai production.

## Ghi chú

- Các tính năng mới được phát triển trên nhánh riêng rồi mới tạo Pull Request.
- `README.md` giữ nguyên nội dung ban đầu.
- Không lưu API key thật trong repository.
