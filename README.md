# Live Chatting Application

## Requirements

- **Node.js** 18+ (for frontend)
- **Python** 3.11+ (for backend)
- **PostgreSQL** (database)
- **just** (optional, for convenience commands)

## For development or running it

```bash
# 1. Build frontend
cd ./client && npm run build

# 2. Start server (serves API + WebSocket + frontend on :8000)
cd ../server
pip install -r requirements.txt
cp .env.example .env  # edit DATABASE_URL if needed
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Rebuild frontend (`npm run build` in `client/`) after changes.

## Using `just`

```bash
# Install dependencies
just install

# Development (builds frontend + FastAPI with hot reload)
just dev

# Production (builds frontend, runs server)
just run
```

Run `just` to see all available commands.
