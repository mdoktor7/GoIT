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
        logging.info(f'{ws.remote_address} connects')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects')

    async def send_to_clients(self, message: str):
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

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
            if message.startswith("exchange"):
                parts = message.split()
                try:
                    days = int(parts[1]) if len(parts) > 1 else 1
                    days = min(days, 10)
                except ValueError:
                    await self.send_to_clients("Invalid number of days. Please provide a number between 1 and 10.")
                    continue

                exchange = await get_exchange(days)
                await self.send_to_clients(exchange)

                # Log the command execution
                logging_service = LoggingService()
                await logging_service.log_command(f"exchange rates for {SUPPORTED_CURRENCIES} over last {days} days")
            elif message == 'Hello server':
                await self.send_to_clients("Привіт мої карапузи!")
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    asyncio.run(main())


