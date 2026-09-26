# Hướng dẫn phát triển

## Yêu cầu

- Python 3.11 trở lên
- Git

## Cài đặt backend

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
Copy-Item .env.example .env
```

## Chạy API

```powershell
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

Kiểm tra tại:

- API: http://127.0.0.1:8000
- Health check: http://127.0.0.1:8000/health
- Swagger: http://127.0.0.1:8000/docs


## Chạy kiểm thử

```powershell
pytest
```

## Quy tắc bảo mật

- Không commit file `.env` hoặc API key.
- Chỉ đưa biến cấu hình không nhạy cảm vào `.env.example`.
- Không gửi API key từ frontend.
