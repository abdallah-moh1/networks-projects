from app.managers.communication_manager import CommunicationManager


class MessageHandlers:
    """Handlers for incoming WebSocket message types."""

    @staticmethod
    async def handle_sync_request(username: str, message: dict[str, object]) -> None:
        await CommunicationManager.send_json(
            username,
            {
                "type": "message_received",
                "message_type": "sync_request",
                "message": message,
            },
        )

    @staticmethod
    async def handle_send_message(username: str, message: dict[str, object]) -> None:
        await CommunicationManager.send_json(
            username,
            {
                "type": "message_received",
                "message_type": "send_message",
                "message": message,
            },
        )

    @staticmethod
    async def handle_confirm_delivery(
        username: str, message: dict[str, object]
    ) -> None:
        await CommunicationManager.send_json(
            username,
            {
                "type": "message_received",
                "message_type": "confirm_delivery",
                "message": message,
            },
        )

    @staticmethod
    async def handle_confirm_seen(username: str, message: dict[str, object]) -> None:
        await CommunicationManager.send_json(
            username,
            {
                "type": "message_received",
                "message_type": "confirm_seen",
                "message": message,
            },
        )
