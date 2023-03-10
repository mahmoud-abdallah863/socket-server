import websockets
import asyncio


async def listen():
    url = "ws://192.168.1.103:44445"
    async with websockets.connect(url) as ws:
        await ws.send("Hello server")
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())
