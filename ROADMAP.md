# ROADMAP - AI Tra Cứu Chuẩn Độ

## 1. Mục tiêu dự án

Xây dựng một ứng dụng AI trên website chuẩn độ, có khả năng:

- Tra cứu tài liệu hóa học liên quan đến chuẩn độ.
- Trả lời câu hỏi dựa trên tài liệu được cung cấp.
- Hỗ trợ tính toán các bài toán chuẩn độ.
- Giải thích công thức, phương trình phản ứng và từng bước tính.
- Giúp người học kiểm tra và hiểu kết quả, không chỉ đưa ra đáp án.

## 2. Phạm vi phiên bản đầu tiên (MVP)

### 2.1. Tra cứu tài liệu

- Cho phép người dùng đặt câu hỏi bằng tiếng Việt.
- Tra cứu tài liệu về:
  - Chuẩn độ axit - bazơ.
  - Chuẩn độ oxi hóa - khử.
  - Chuẩn độ kết tủa.
  - Chuẩn độ tạo phức.
  - Chất chỉ thị và điểm tương đương.
  - Quy trình và an toàn thí nghiệm.
- Hiển thị câu trả lời kèm nguồn tài liệu tham khảo.
- Nếu không tìm thấy thông tin, AI phải thông báo rõ thay vì tự suy đoán.

### 2.2. Hỗ trợ tính toán

- Tính nồng độ dung dịch.
- Tính số mol chất tham gia phản ứng.
- Tính thể tích dung dịch cần dùng.
- Tính theo tỉ lệ phương trình phản ứng.
- Hỗ trợ nhiều lần đo và tính giá trị trung bình.
- Hiển thị công thức, dữ liệu đầu vào, các bước giải và kết quả.
- Kiểm tra dữ liệu đầu vào và cảnh báo đơn vị không hợp lệ.

## 3. Nguyên tắc kỹ thuật

- Không để API key ở phía frontend.
- Các phép tính hóa học phải do module tính toán xác định thực hiện; AI chỉ giải thích và hướng dẫn.
- Câu trả lời tra cứu phải ưu tiên dữ liệu trong tài liệu của dự án.
- Mọi kết quả cần hiển thị đơn vị rõ ràng.
- Có cảnh báo rằng kết quả AI không thay thế hướng dẫn an toàn trong phòng thí nghiệm.
- Thiết kế hệ thống để có thể bổ sung tài liệu và công thức mới.

## 4. Lộ trình phát triển

### Giai đoạn 0 - Khởi tạo dự án

- [ ] Tạo cấu trúc thư mục frontend, backend và tài liệu.
- [ ] Chọn stack kỹ thuật.
- [ ] Thiết lập Git, biến môi trường và quy tắc bảo mật.
- [ ] Viết tài liệu hướng dẫn cài đặt và chạy dự án.

### Giai đoạn 1 - Bộ tính toán hóa học

- [ ] Xây dựng module tính số mol, nồng độ và thể tích.
- [ ] Hỗ trợ hệ số phản ứng trong phương trình hóa học.
- [ ] Xử lý đơn vị mL/L và mmol/mol.
- [ ] Kiểm tra dữ liệu âm, bằng 0, thiếu dữ liệu hoặc sai đơn vị.
- [ ] Viết test cho các bài toán chuẩn độ mẫu.

### Giai đoạn 2 - Giao diện website

- [ ] Tạo trang giới thiệu dự án.
- [ ] Tạo biểu mẫu nhập dữ liệu chuẩn độ.
- [ ] Tạo khu vực hiển thị các bước tính.
- [ ] Tạo giao diện hỏi đáp AI.
- [ ] Thiết kế responsive cho điện thoại và máy tính.

### Giai đoạn 3 - AI hỏi đáp cơ bản

- [ ] Tạo backend nhận câu hỏi từ website.
- [ ] Kết nối mô hình AI thông qua API hoặc mô hình tự triển khai.
- [ ] Thiết lập system prompt chuyên về chuẩn độ.
- [ ] Phân biệt câu hỏi tra cứu và câu hỏi tính toán.
- [ ] Kết hợp module tính toán khi người dùng cần tính kết quả.
- [ ] Thêm giới hạn tần suất và xử lý lỗi API.

### Giai đoạn 4 - Tra cứu tài liệu bằng RAG

- [ ] Thu thập tài liệu được phép sử dụng.
- [ ] Chuẩn hóa tài liệu PDF, DOCX và TXT.
- [ ] Chia tài liệu thành các đoạn phù hợp.
- [ ] Tạo embedding và lưu vào vector database.
- [ ] Tìm các đoạn liên quan trước khi gửi câu hỏi cho AI.
- [ ] Hiển thị tên tài liệu và vị trí tham khảo trong câu trả lời.
- [ ] Cho phép quản trị viên bổ sung hoặc cập nhật tài liệu.

### Giai đoạn 5 - Kiểm thử và cải thiện chất lượng

- [ ] Tạo bộ câu hỏi chuẩn về chuẩn độ.
- [ ] Kiểm tra độ chính xác của công thức và kết quả.
- [ ] Kiểm tra AI có trích dẫn đúng tài liệu hay không.
- [ ] Kiểm tra các trường hợp thiếu dữ liệu và dữ liệu sai.
- [ ] Đánh giá thời gian phản hồi và chi phí mỗi câu hỏi.
- [ ] Bổ sung nút báo lỗi câu trả lời.

### Giai đoạn 6 - Triển khai

- [ ] Đưa frontend lên dịch vụ hosting.
- [ ] Đưa backend lên server an toàn.
- [ ] Cấu hình biến môi trường trên môi trường production.
- [ ] Thiết lập domain và HTTPS.
- [ ] Theo dõi lỗi, log và mức sử dụng.
- [ ] Sao lưu cơ sở dữ liệu và tài liệu.

## 5. Kiến trúc đề xuất

```text
Frontend website
    |
    v
Backend API
    |-- Calculator: tính toán xác định
    |-- Retriever: tìm tài liệu liên quan
    |-- AI Service: giải thích và trả lời
    |-- Database: người dùng, lịch sử, tài liệu
    `-- Vector Database: embedding tài liệu
```

## 6. Công nghệ đề xuất

- Frontend: HTML/CSS/JavaScript hoặc React.
- Backend: Python FastAPI.
- Tính toán: Python thuần, có thể bổ sung SymPy khi cần.
- AI: API mô hình ngôn ngữ hoặc mô hình mã nguồn mở.
- Vector database: ChromaDB hoặc FAISS cho bản đầu tiên.
- Cơ sở dữ liệu: SQLite khi phát triển, PostgreSQL khi triển khai.
- Kiểm thử: pytest cho backend và module tính toán.

## 7. Tiêu chí hoàn thành MVP

- Người dùng hỏi được câu hỏi bằng tiếng Việt.
- AI trả lời dựa trên tài liệu chuẩn độ đã nạp.
- Người dùng nhập số liệu và nhận được kết quả tính đúng.
- Kết quả có công thức, đơn vị và từng bước giải.
- API key không xuất hiện trong mã frontend.
- Có test cho các công thức tính chính.
- Website hoạt động tốt trên điện thoại và máy tính.

## 8. Các tính năng có thể phát triển sau

- Đọc dữ liệu từ ảnh chụp phiếu thí nghiệm.
- Vẽ đường cong chuẩn độ.
- Phân tích điểm tương đương từ dữ liệu thực nghiệm.
- Đăng nhập và lưu lịch sử bài tập.
- Chế độ giáo viên tạo bài tập.
- Xuất lời giải thành PDF.
- Hỗ trợ tiếng Anh.
