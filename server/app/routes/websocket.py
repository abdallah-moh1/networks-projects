import json

from app.managers import CommunicationManager, connection_manager
from app.utils import logger
from fastapi import APIRouter, WebSocket

router = APIRouter(prefix="/ws")


@router.websocket("")
async def websocket_endpoint(websocket: WebSocket, username: str):
    # TODO: validate the access token and resolve the username from it.
    client_ip = websocket.client.host if websocket.client else "unknown"
    await connection_manager.connect(username, websocket, client_ip)

    try:
        while True:
            try:
                message = await websocket.receive_json()
            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON from user {username!r} at {client_ip}")
                if connection_manager.get_connection(username) is not websocket:
                    break
                await CommunicationManager.send_error(
                    username,
                    "invalid_json",
                    "WebSocket message must contain valid JSON.",
                )
                continue

            if connection_manager.get_connection(username) is not websocket:
                logger.debug(
                    f"Ignoring a message from a replaced connection for "
                    f"{username!r} at {client_ip}"
                )
                break

            await CommunicationManager.handle_message(
                username=username,
                client_ip=client_ip,
                message=message,
            )
    finally:
        await connection_manager.disconnect(
            username=username,
            websocket=websocket,
            client_ip=client_ip,
        )
