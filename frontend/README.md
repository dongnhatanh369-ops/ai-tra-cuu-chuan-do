# Frontend

Giao diện thử nghiệm cho Giai đoạn 1, dùng để kiểm tra luồng hỏi đáp AI trước khi tích hợp vào website hiện tại.

Chạy thử bằng static server:

```powershell
python -m http.server 5500 --directory frontend
```

Mở `http://127.0.0.1:5500`. Frontend gọi `POST http://127.0.0.1:8000/api/v1/ai/chat` với `{ "question": "..." }` và chờ response `{ "answer": "..." }`.
