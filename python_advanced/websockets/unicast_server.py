#!/usr/bin/env python3
"""WebSocket server that validates incoming messages."""
import asyncio

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    """Start the server and keep it running forever."""
    async with serve(connection_handler, "127.0.0.1", 8765) as server:
        await server.serve_forever()
if __name__ == "__main__":
    asyncio.run(main())
