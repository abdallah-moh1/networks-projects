# Live Chatting Application

## For development or running it

```bash
# 1. Build frontend
cd ../client && npm run build

# 2. Start server (serves API + WebSocket + frontend on :8000)
cd ../server
pip install -r requirements.txt
cp .env.example .env  # edit DATABASE_URL if needed
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

- API at `http://<lan-ip>:8000/api/health`
- WebSocket at `ws://<lan-ip>:8000/ws`
- Frontend at `http://<lan-ip>:8000/`

Rebuild frontend (`npm run build` in `client/`) after changes.
