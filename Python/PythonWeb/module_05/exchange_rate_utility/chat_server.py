import asyncio
import websockets
import json
from services.exchange_service import ExchangeService
from services.logging_service import LoggingService
from constants import SUPPORTED_CURRENCIES

connected_users = set()


async def send_to_all(message):
    if connected_users:
        await asyncio.wait([user.send(message) for user in connected_users])


async def handle_exchange_command(days):
    exchange_service = ExchangeService()
    days = min(days, 10)
    exchange_data = await exchange_service.get_exchange_rates(SUPPORTED_CURRENCIES, days)
    return json.dumps(exchange_data)


async def handler(websocket, path):
    connected_users.add(websocket)
    logging_service = LoggingService()
    
    try:
        async for message in websocket:
            data = json.loads(message)
            if data['command'] == 'exchange':
                days = int(data.get('days', 1))
                exchange_data = await handle_exchange_command(days)
                await websocket.send(exchange_data)
                await logging_service.log_command(f"exchange command with {days} days")
    finally:
        connected_users.remove(websocket)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
