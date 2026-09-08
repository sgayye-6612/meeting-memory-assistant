import asyncio
import websockets


async def test():
    async with websockets.connect("ws://127.0.0.1:8000/ws/meeting") as ws:
        response = await ws.recv()
        print("SERVER:", response)

        await ws.send("We decided to launch the product next Monday.")

        response = await ws.recv()
        print("SERVER:", response)


asyncio.run(test())
