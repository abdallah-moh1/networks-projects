from types import MappingProxyType

from app.managers.connection_manager import connection_manager
from app.utils import logger


class CommunicationManager:
    """Dispatch incoming WebSocket messages by protocol type."""

    _HANDLERS = MappingProxyType(
        {
            "sync_request": "handle_sync_request",
            "send_message": "handle_send_message",
            "confirm_delivery": "handle_confirm_delivery",
            "confirm_seen": "handle_confirm_seen",
        }
    )

    @staticmethod
    async def handle_message(
        username: str,
        client_ip: str,
        message: object,
    ) -> None:
        if not isinstance(message, dict):
            logger.warning(
                f"Invalid WebSocket message from user {username!r} at {client_ip}"
            )
            await CommunicationManager.send_error(
                username,
                "invalid_message",
                "Expected a JSON object.",
            )
            return

        message_type = message.get("type")
        if not isinstance(message_type, str):
            logger.warning(
                f"WebSocket message without a valid type from user {username!r} "
                f"at {client_ip}"
            )
            await CommunicationManager.send_error(
                username,
                "missing_message_type",
                "Message must include a string 'type'.",
            )
            return

        logger.info(
            f"WebSocket request from user {username!r} at {client_ip}: "
            f"type={message_type[:64]!r}"
        )

        handler_name = CommunicationManager._HANDLERS.get(message_type)
        if handler_name is None:
            await CommunicationManager.send_error(
                username,
                "unknown_message_type",
                f"Unknown message type '{message_type}'.",
            )
            return

        from app.handlers import MessageHandlers

        handler = getattr(MessageHandlers, handler_name)
        await handler(username, message)

    @staticmethod
    async def send_json(username: str, message: dict[str, object]) -> None:
        websocket = connection_manager.get_connection(username)
        message_type = message.get("type", "unknown")
        if websocket is None:
            logger.warning(
                f"Cannot send WebSocket message type {message_type!r} to "
                f"{username!r}: no active connection"
            )
            return

        try:
            await websocket.send_json(message)
        except (OSError, RuntimeError):
            logger.warning(
                f"Failed to send WebSocket message type {message_type!r} "
                f"to {username!r}"
            )

    @staticmethod
    async def send_error(
        username: str,
        error_code: str,
        error_detail: str,
    ) -> None:
        await CommunicationManager.send_json(
            username,
            {
                "type": "error",
                "error_code": error_code,
                "error_detail": error_detail,
            },
        )
