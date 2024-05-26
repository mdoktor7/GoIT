import asyncio
import websockets
import json


async def send_exchange_command(uri, command, days):
    async with websockets.connect(uri) as websocket:
        # Send the command
        await websocket.send(json.dumps({'command': command, 'days': days}))
        
        # Wait for the response
        response = await websocket.recv()
        print(f"Received: {response}")


async def main():
    uri = "ws://localhost:8765"
    await send_exchange_command(uri, 'exchange', 10)  # Example command

if __name__ == "__main__":
    asyncio.run(main())
