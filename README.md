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

# 2. Start server
cd ../server
pip install -r requirements.txt
cp .env.example .env  # edit DATABASE_URL, HOST, or PORT if needed

# Run in Development mode (with auto-reload)
python -m app.main

# Or run in Production mode (without reload)
python -m app.main --prod
```

Host and port are automatically read from `server/.env` (`HOST=0.0.0.0` and `PORT=8000` by default).

Rebuild frontend (`npm run build` in `client/`) after changes.

## Using `just`

```bash
# Install dependencies
just install

# Development (builds frontend + starts FastAPI with hot reload)
just dev

# Production (builds frontend, runs server without reload)
just run
```

Run `just` to see all available commands.
