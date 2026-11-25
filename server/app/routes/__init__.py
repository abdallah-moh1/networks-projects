from app.routes.health import router as health_router
from app.routes.websocket import router as websocket_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api")
api_router.include_router(health_router)
api_router.include_router(websocket_router)

__all__ = ["api_router"]
