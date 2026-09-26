# ROADMAP - AI Tra Cứu Chuẩn Độ

## Mục tiêu

Xây dựng AI backend cho website chuẩn độ hiện có, có khả năng tra cứu tài liệu và hỗ trợ tính toán hóa học. Website hiện tại sẽ được tích hợp sau khi API AI ổn định.

## Nguyên tắc phát triển

- Ưu tiên phát triển AI backend trước, không xây dựng lại frontend.
- Phép tính hóa học phải do module xác định thực hiện.
- AI dùng để hiểu câu hỏi, tra cứu tài liệu và giải thích kết quả.
- API key và dữ liệu nhạy cảm chỉ được lưu ở backend.
- Các API phải được thiết kế để website hiện tại dễ dàng tích hợp.

## Giai đoạn 0 - Khởi tạo nền tảng

- [x] Tạo repository và nhánh `main`.
- [x] Tạo cấu trúc backend, frontend placeholder và thư mục tài liệu.
- [x] Chọn Python/FastAPI làm nền tảng backend.
- [x] Tạo file cấu hình dự án và `.env.example`.
- [x] Tạo API health check.
- [x] Viết hướng dẫn cài đặt và chạy dự án.

## Giai đoạn 1 - Xây dựng AI backend cơ bản

- [ ] Xác định interface API cho website hiện tại.
- [ ] Tạo endpoint hỏi đáp AI.
- [ ] Tạo system prompt chuyên về hóa học và chuẩn độ.
- [ ] Phân loại câu hỏi: tra cứu, tính toán, quy trình và an toàn.
- [ ] Xử lý lỗi, timeout và giới hạn tần suất gọi AI.
- [ ] Thiết lập logging và cấu trúc phản hồi thống nhất.
- [ ] Viết test cho API và các tình huống lỗi.

## Giai đoạn 2 - Bộ tính toán chuẩn độ

- [ ] Tính số mol, nồng độ và thể tích.
- [ ] Hỗ trợ hệ số phương trình phản ứng.
- [ ] Hỗ trợ đơn vị mL/L và mmol/mol.
- [ ] Tính giá trị trung bình từ nhiều lần chuẩn độ.
- [ ] Kiểm tra dữ liệu đầu vào và cảnh báo đơn vị sai.
- [ ] Trả về công thức và từng bước giải.
- [ ] Đảm bảo AI không tự tính thay cho module xác định.

## Giai đoạn 3 - Tra cứu tài liệu bằng RAG

- [ ] Thu thập và chuẩn hóa tài liệu chuẩn độ được phép sử dụng.
- [ ] Đọc PDF, DOCX và TXT.
- [ ] Chia tài liệu thành các đoạn nhỏ.
- [ ] Tạo embedding và lưu vào vector database.
- [ ] Tìm đoạn tài liệu liên quan theo câu hỏi.
- [ ] Gửi ngữ cảnh tìm được cho AI để tạo câu trả lời.
- [ ] Trả về nguồn tài liệu và thông tin tham khảo.
- [ ] Thông báo rõ khi không có đủ dữ liệu để trả lời.

## Giai đoạn 4 - Kết hợp AI, tra cứu và tính toán

- [ ] Cho AI tự nhận diện khi nào cần gọi bộ tính toán.
- [ ] Kết hợp kết quả tính toán với tài liệu tham khảo.
- [ ] Chuẩn hóa format trả lời cho website.
- [ ] Hỗ trợ lịch sử hội thoại theo phiên.
- [ ] Thêm cơ chế đánh giá và báo lỗi câu trả lời.
- [ ] Kiểm thử bằng bộ câu hỏi chuẩn ngành hóa học.

## Giai đoạn 5 - Tích hợp website hiện tại

- [ ] Xác định công nghệ và API hiện có của website.
- [ ] Thêm lớp gọi API AI vào website.
- [ ] Tích hợp khung chat hoặc form tra cứu vào giao diện sẵn có.
- [ ] Hiển thị công thức, nguồn tài liệu và kết quả tính.
- [ ] Kiểm tra xác thực, CORS và phân quyền.
- [ ] Kiểm thử end-to-end giữa website và backend AI.

## Giai đoạn 6 - Triển khai và vận hành

- [ ] Đưa backend lên môi trường production.
- [ ] Cấu hình biến môi trường và HTTPS.
- [ ] Theo dõi lỗi, thời gian phản hồi và chi phí AI.
- [ ] Sao lưu cơ sở dữ liệu và vector database.
- [ ] Thiết lập quy trình cập nhật tài liệu.
- [ ] Bổ sung phân quyền quản trị viên.

## Tiêu chí MVP

- Người dùng gửi được câu hỏi tiếng Việt qua API.
- AI trả lời theo tài liệu chuẩn độ được cung cấp.
- Bộ tính toán cho kết quả đúng và có đơn vị.
- Kết quả có công thức, từng bước giải và nguồn tham khảo.
- Website hiện tại có thể gọi API bằng HTTP.
- API key không xuất hiện ở frontend.
