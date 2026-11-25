import time

from app.utils.logger import logger
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        ip = request.client.host if request.client else "unknown"

        try:
            response = await call_next(request)
            duration = round((time.time() - start) * 1000, 2)
            msg = f"{request.method} {request.url.path} - {response.status_code} from {ip} ({duration}ms)"

            if response.status_code >= 500:
                logger.error(msg)
            elif response.status_code >= 400:
                logger.warning(msg)
            else:
                logger.info(msg)

            return response
        except Exception:
            duration = round((time.time() - start) * 1000, 2)
            logger.error(
                f"{request.method} {request.url.path} - 500 from {ip} ({duration}ms)"
            )
            raise
