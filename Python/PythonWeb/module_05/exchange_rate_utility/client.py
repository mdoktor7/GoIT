import asyncio
import websockets
import json
import logging

logging.basicConfig(level=logging.INFO)

async def send_exchange_command(uri, command, days):
    try:
        async with websockets.connect(uri) as websocket:
            logging.info(f"Connected to server at {uri}")

            # Send the command
            message = json.dumps({'command': command, 'days': days})
            logging.info(f"Sending message: {message}")
            await websocket.send(message)
            
            # Wait for the response
            response = await websocket.recv()
            logging.info(f"Received response: {response}")
            print(f"Received: {response}")
    except Exception as e:
        logging.error(f"Error: {e}")

async def main():
    uri = "ws://localhost:9090"
    await send_exchange_command(uri, 'exchange', 2)  # Example command

if __name__ == "__main__":
    asyncio.run(main())

