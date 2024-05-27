import aiohttp
import asyncio
import logging
from aiohttp import ClientSession
from constants import PRIVATBANK_API_URL

logging.basicConfig(level=logging.INFO)

async def fetch_exchange_rates(session: ClientSession, date: str):
    url = PRIVATBANK_API_URL.format(date)
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to fetch exchange rates for {date}: {e}")
        raise

async def fetch_rates_for_days(dates):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_exchange_rates(session, date) for date in dates]
        return await asyncio.gather(*tasks)
