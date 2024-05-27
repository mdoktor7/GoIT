import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import asyncio
import logging
import json
import names
import websockets
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK
from services import ExchangeService, LoggingService
from constants import SUPPORTED_CURRENCIES

logging.basicConfig(level=logging.INFO)

async def get_exchange(days: int):
    exchange_service = ExchangeService()
    exchange_data = await exchange_service.get_exchange_rates(SUPPORTED_CURRENCIES, days)
    return json.dumps(exchange_data)

class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logging.info(f'{ws.remote_address} connects as {ws.name}')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} ({ws.name}) disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            await asyncio.wait([asyncio.create_task(client.send(message)) for client in self.clients])

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distribute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            logging.info(f"Received message: {message}")
            if message.startswith("exchange"):
                parts = message.split()
                days = int(parts[1]) if len(parts) > 1 else 1
                days = min(days, 10)
                exchange = await get_exchange(days)
                await self.send_to_clients(exchange)
            elif message == 'Hello server':
                await self.send_to_clients("Привіт мої карапузи!")
            else:
                await self.send_to_clients(f"{ws.name}: {message}")

async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 9090):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())


