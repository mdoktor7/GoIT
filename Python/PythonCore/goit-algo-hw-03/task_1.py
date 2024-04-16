from datetime import datetime


def get_days_from_today():
    while True:
        try:
            date = input("Enter a date in the format 'YYYY-MM-DD':  ")
            date_formatted = datetime.strptime(date, "%Y-%m-%d")
            date_now = datetime.today()
            days_from_today = (date_now - date_formatted).days

            if days_from_today >= 0:
                print(f"{days_from_today} days have passed since the date {date}")
            else:
                print(f"{abs(days_from_today)} days before the date {date}")

            return days_from_today
        except ValueError:
            print(f"Please enter the date {date} in format Year-Month-Day")


get_days_from_today()