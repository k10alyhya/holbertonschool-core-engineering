#!/usr/bin/env python3
"""ASGI app serving an HTML page and a WebSocket echo endpoint."""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    """Return the home page."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    """Accept the connection and echo every text message."""
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)
    await websocket.close()

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
