# PROGRESS - AI Tra Cứu Chuẩn Độ

## Trạng thái hiện tại

- Nhánh chính: `main`
- Nhánh phát triển tích hợp: `feature/integrated-ai`
- Trạng thái: Đang phát triển AI backend

## Đã hoàn thành trên main

### Giai đoạn 0 - Khởi tạo dự án

- [x] Tạo repository và nhánh `main`.
- [x] Tạo cấu trúc backend, frontend placeholder, tài liệu và dữ liệu.
- [x] Chọn Python/FastAPI làm nền tảng backend.
- [x] Tạo cấu hình dự án, `.env.example` và `.gitignore`.
- [x] Tạo API health check tại `GET /health`.
- [x] Viết hướng dẫn phát triển.
- [x] Cập nhật roadmap.

## Đã hoàn thành trên nhánh phát triển

### Frontend - `feature/integrated-ai`

- [x] Giao diện chat AI thử nghiệm.
- [x] Responsive cho điện thoại, máy tính bảng và desktop.
- [x] Hỗ trợ tiếng Việt và English.
- [x] Lưu lựa chọn ngôn ngữ bằng `localStorage`.
- [x] Hỗ trợ màn hình cảm ứng, dọc/ngang và safe area.

### Giai đoạn 2 - `feature/titration-calculator`

- [x] Bộ tính số mol, nồng độ và thể tích.
- [x] Hỗ trợ hệ số phương trình phản ứng và đơn vị mL/L.
- [x] API `POST /api/v1/titration/calculate`.

### Giai đoạn 3 - `feature/document-rag`

- [x] Nạp tài liệu Markdown/TXT.
- [x] Chia tài liệu thành các đoạn nhỏ.
- [x] Tìm kiếm đoạn liên quan theo từ khóa.
- [x] API `POST /api/v1/documents/search`.

## Đang thực hiện

- [ ] Thiết kế API backend hỏi đáp AI.
- [ ] Kết nối mô hình AI.
- [ ] Xây dựng system prompt chuyên về chuẩn độ.
- [ ] Bổ sung embedding và vector database.
- [ ] Kết nối frontend với backend thật.

## Chưa thực hiện

- [ ] Đọc tài liệu PDF/DOCX.
- [ ] Tích hợp vào website hiện tại.
- [ ] Kiểm thử end-to-end.
- [ ] Triển khai production.

## Ghi chú

- Code mới vẫn ở các nhánh phát triển, chưa nhập vào `main`.
- `README.md` được giữ nguyên nội dung ban đầu.
- Không lưu API key thật trong repository.
