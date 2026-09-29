# ROADMAP - AI Tra Cứu Chuẩn Độ

## Mục tiêu

Xây dựng AI backend cho website chuẩn độ hiện có, có khả năng tra cứu tài liệu và hỗ trợ tính toán hóa học. Website hiện tại sẽ được tích hợp sau khi API AI ổn định.

## Trạng thái tổng quan

| Hạng mục | Trạng thái | Nhánh/ghi chú |
|---|---|---|
| Giai đoạn 0 - Khởi tạo nền tảng | Hoàn thành | `main` |
| Frontend prototype responsive và đa ngôn ngữ | Hoàn thành | `feature/integrated-ai` |
| Giai đoạn 1 - AI backend cơ bản | Chưa hoàn thành | Ưu tiên tiếp theo |
| Giai đoạn 2 - Bộ tính toán chuẩn độ | Hoàn thành bản cơ bản | `feature/titration-calculator` |
| Giai đoạn 3 - Tra cứu tài liệu bước đầu | Hoàn thành bản cơ bản | `feature/document-rag` |
| Giai đoạn 4 - Kết hợp AI, tra cứu và tính toán | Chưa hoàn thành | Phụ thuộc Giai đoạn 1-3 |
| Giai đoạn 5 - Tích hợp website hiện tại | Chưa hoàn thành | Chờ API AI ổn định |
| Giai đoạn 6 - Triển khai và vận hành | Chưa hoàn thành | Sau MVP |

## Nguyên tắc phát triển

- Ưu tiên phát triển AI backend trước, không xây dựng lại frontend.
- Phép tính hóa học phải do module xác định thực hiện.
- AI dùng để hiểu câu hỏi, tra cứu tài liệu và giải thích kết quả.
- API key và dữ liệu nhạy cảm chỉ được lưu ở backend.
- Code mới phát triển trên nhánh riêng rồi mới tạo Pull Request vào `main`.

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

## Giao diện hỗ trợ Giai đoạn 1

- [x] Giao diện chat thử nghiệm.
- [x] Responsive cho điện thoại, máy tính bảng và desktop.
- [x] Hỗ trợ tiếng Việt và English.
- [x] Lưu lựa chọn ngôn ngữ bằng `localStorage`.
- [x] Hỗ trợ màn hình cảm ứng, dọc/ngang và safe area.
- [ ] Kết nối với backend AI thật.
- [ ] Tích hợp vào website hiện tại.

## Giai đoạn 2 - Bộ tính toán chuẩn độ

- [x] Tính số mol, nồng độ và thể tích.
- [x] Hỗ trợ hệ số phương trình phản ứng.
- [x] Hỗ trợ đơn vị mL/L.
- [x] Tính giá trị trung bình từ nhiều lần chuẩn độ.
- [x] Kiểm tra dữ liệu đầu vào và cảnh báo đơn vị sai.
- [x] Trả về công thức và từng bước giải qua API.
- [x] Tách module tính toán khỏi AI.
- [ ] Bổ sung hỗ trợ mmol/mol và các bài toán nâng cao.
- [ ] Tích hợp API vào website hiện tại.

## Giai đoạn 3 - Tra cứu tài liệu bằng RAG

- [x] Nạp và chuẩn hóa tài liệu Markdown/TXT.
- [x] Chia tài liệu thành các đoạn nhỏ.
- [x] Tìm đoạn tài liệu liên quan theo từ khóa.
- [x] Tạo API tìm kiếm tài liệu.
- [ ] Đọc tài liệu PDF và DOCX.
- [ ] Tạo embedding và lưu vào vector database.
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

- [ ] Người dùng gửi được câu hỏi tiếng Việt qua API AI.
- [x] Bộ tính toán có kết quả và đơn vị cho các trường hợp cơ bản.
- [x] API tìm kiếm được tài liệu Markdown/TXT.
- [ ] AI trả lời theo tài liệu chuẩn độ được cung cấp.
- [ ] Kết quả có công thức, từng bước giải và nguồn tham khảo.
- [ ] Website hiện tại có thể gọi API bằng HTTP.
- [x] API key không xuất hiện ở frontend.
