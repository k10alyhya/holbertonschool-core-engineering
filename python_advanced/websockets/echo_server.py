#!/usr/bin/env python3


import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    server = await serve(connection_handler, "127.0.0.1", 8765)

    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
