import socket
from contextlib import asynccontextmanager
from pathlib import Path

from app.config import HOST, PORT
from app.db.db import close_db, init_db
from app.routes import api_router
from app.utils.logger import logger
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    # Print LAN IP for mobile connections
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        lan_ip = s.getsockname()[0]
        s.close()
        logger.info(f"Server running on LAN: http://{lan_ip}:{PORT}")
    except Exception:
        logger.info(f"Server running on http://{HOST}:{PORT}")
    yield
    await close_db()


app = FastAPI(title="Messaging API", lifespan=lifespan)

# Include main API router
app.include_router(api_router)

# Serve built frontend
DIST_DIR = Path(__file__).resolve().parent.parent.parent / "client" / "dist"

if DIST_DIR.exists():
    # Static assets (JS, CSS, images, etc.)
    app.mount("/assets", StaticFiles(directory=str(DIST_DIR / "assets")), name="assets")

    # SPA fallback: serve index.html for all non-API, non-asset routes
    @app.get("/{full_path:path}")
    async def spa_fallback(full_path: str):
        index_file = DIST_DIR / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        return {"error": "Frontend not built. Run `npm run build` in client/"}
else:
    logger.error(f"Frontend build not found: {DIST_DIR}")
