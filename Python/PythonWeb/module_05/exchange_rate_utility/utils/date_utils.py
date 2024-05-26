import datetime


def get_last_n_days(n: int):
    today = datetime.date.today()
    return [(today - datetime.timedelta(days=i)).strftime('%d.%m.%Y') for i in range(n)]


def validate_days(days):
    return 1 <= days <= 10
