from utils.http_utils import fetch_rates_for_days
from utils.date_utils import get_last_n_days
from constants import SUPPORTED_CURRENCIES, MAX_DAYS


class ExchangeService:
    def __init__(self, supported_currencies=None):
        self.supported_currencies = supported_currencies or SUPPORTED_CURRENCIES


    async def get_exchange_rates(self, currencies, days):
        days = min(days, MAX_DAYS)
        dates = get_last_n_days(days)
        results = await fetch_rates_for_days(dates)

        exchange_data = {}
        for date, result in zip(dates, results):
            rates = {rate['currency']: rate['saleRate'] for rate in result['exchangeRate'] if rate['currency'] in currencies}
            exchange_data[date] = rates

        return exchange_data

