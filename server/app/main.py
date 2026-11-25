import sys
from contextlib import asynccontextmanager

from app.config import HOST, PORT
from app.db import close_db, init_db
from app.frontend import mount_frontend
from app.routes import api_router
from app.utils import get_lan_ip, logger
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    lan_ip = get_lan_ip()
    if lan_ip:
        logger.info(f"Server running on LAN: http://{lan_ip}:{PORT}")
    else:
        logger.info(f"Server running on http://{HOST}:{PORT}")

    yield
    await close_db()


def create_app() -> FastAPI:
    app = FastAPI(title="Messaging API", lifespan=lifespan)
    app.include_router(api_router)
    mount_frontend(app)
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    reload = "--prod" not in sys.argv
    uvicorn.run(
        "app.main:app",
        host=HOST,
        port=PORT,
        reload=reload,
        access_log=False,
        log_level="critical",
    )
