from app.routes.health import router as health_router
from fastapi import APIRouter

# Main API router with /api prefix
api_router = APIRouter(prefix="/api")
api_router.include_router(health_router)

__all__ = ["api_router"]
