from pathlib import Path

from app.config import CLIENT_DIST_DIR
from app.utils.logger import logger
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


def mount_frontend(app: FastAPI, dist_dir: Path = CLIENT_DIST_DIR) -> None:
    if not dist_dir.exists():
        logger.error(f"Frontend build not found: {dist_dir}")
        return

    assets_dir = dist_dir / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def spa_fallback(full_path: str):
        if full_path.split("/")[0] in ("api", "assets"):
            raise HTTPException(status_code=404, detail="Not found")

        index_file = dist_dir / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        return {"error": "Frontend not built. Run `npm run build` in client/"}
