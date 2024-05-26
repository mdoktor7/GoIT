import argparse
import asyncio
from services.exchange_service import ExchangeService
from services.logging_service import LoggingService
from constants import SUPPORTED_CURRENCIES
from utils.date_utils import validate_days

# def validate_days(days):
#     return 1 <= days <= 10


async def main(days):
    exchange_service = ExchangeService()
    logging_service = LoggingService()

    # if len(sys.argv) != 2:
    #     print("Usage: py .\\main.py <number_of_days>")
    #     return

    if not validate_days(days):
        print("Error: The number of days should not exceed 10.")
        return

    try:
        exchange_rates = await exchange_service.get_exchange_rates(SUPPORTED_CURRENCIES, days)
        for date, rates in exchange_rates.items():
            print(f"{date}: {rates}")

        await logging_service.log_command(f"exchange rates for {SUPPORTED_CURRENCIES} over last {days} days")
    except Exception as e:
        print(f"An error occurred: {e}")
        await logging_service.log_command(f"error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch exchange rates from PrivatBank")
    parser.add_argument('days', type=int, help='Number of days to fetch rates for (max 10)')
    args = parser.parse_args()

    asyncio.run(main(args.days))

# import argparse
# import asyncio
# from services.exchange_service import ExchangeService
# from services.logging_service import LoggingService
# from constants import SUPPORTED_CURRENCIES
#
#
# async def main(days):
#     exchange_service = ExchangeService()
#     logging_service = LoggingService()
#
#     if len(sys.argv) != 2:
#         print("Usage: py .\\main.py <number_of_days>")
#         return
#
#     try:
#         days = int(sys.argv[1])
#     except ValueError:
#         print("Please enter a valid number for days.")
#         return
#
#     if not validate_days(days):
#         print("Error: The number of days should not exceed 10.")
#         return
#     try:
#         exchange_rates = await exchange_service.get_exchange_rates(SUPPORTED_CURRENCIES, days)
#         for date, rates in exchange_rates.items():
#             print(f"{date}: {rates}")
#
#         await logging_service.log_command(f"exchange rates for {SUPPORTED_CURRENCIES} over last {days} days")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         await logging_service.log_command(f"error: {e}")
#         return
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Fetch exchange rates from PrivatBank")
#     parser.add_argument('days', type=int, help='Number of days to fetch rates for (max 10)')
#     args = parser.parse_args()
#     asyncio.run(main(args.days))


#
# async def main():
#     exchange_service = ExchangeService()
#     logging_service = LoggingService()
#
#     if len(sys.argv) != 2:
#         print("Usage: py .\\main.py <number_of_days>")
#         return
#
#     try:
#         days = int(sys.argv[1])
#     except ValueError:
#         print("Please enter a valid number for days.")
#         return
#
#     if not validate_days(days):
#         print("Error: The number of days should not exceed 10.")
#         return
#
#     try:
#         rates = await exchange_service.get_exchange_rates(SUPPORTED_CURRENCIES, days)
#         for rate in rates:
#             print(rate)
#
#         await logging_service.log_command("exchange", days)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
