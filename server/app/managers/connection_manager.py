from app.utils import logger
from fastapi import WebSocket


class ConnectionManager:
    """Track the active WebSocket connection for each username."""

    def __init__(self) -> None:
        self.active_connections: dict[str, WebSocket] = {}
        self._client_ips: dict[str, str] = {}

    async def connect(
        self, username: str, websocket: WebSocket, client_ip: str
    ) -> None:
        await websocket.accept()
        old_websocket = self.active_connections.get(username)
        old_client_ip = self._client_ips.get(username, "unknown")
        self.active_connections[username] = websocket
        self._client_ips[username] = client_ip

        if old_websocket is not None and old_websocket is not websocket:
            logger.info(
                f"Replacing WebSocket for user {username!r} from {old_client_ip} "
                f"with a connection from {client_ip}"
            )
            await self.disconnect(
                username,
                old_websocket,
                reason="Connection replaced",
                client_ip=old_client_ip,
            )
        else:
            logger.info(f"WebSocket connected for user {username!r} from {client_ip}")

    async def disconnect(
        self,
        username: str,
        websocket: WebSocket,
        reason: str = "Connection closed",
        client_ip: str = "unknown",
    ) -> None:
        # Don't remove a newer connection if an older session disconnects later.
        if self.active_connections.get(username) is websocket:
            del self.active_connections[username]
            client_ip = self._client_ips.pop(username, client_ip)
            logger.info(
                f"Removing WebSocket for user {username!r} from {client_ip}: {reason}"
            )
        else:
            logger.debug(
                f"Closing stale WebSocket for user {username!r} from {client_ip}; "
                "keeping the current connection"
            )

        try:
            await websocket.close(code=1000, reason=reason)
            logger.info(
                f"Closed WebSocket for user {username!r} from {client_ip}: {reason}"
            )
        except (OSError, RuntimeError):
            # The socket may already be closed or disconnected.
            logger.debug(
                f"WebSocket for user {username!r} from {client_ip} was already closed"
            )

    def get_connection(self, username: str) -> WebSocket | None:
        return self.active_connections.get(username)


connection_manager = ConnectionManager()
