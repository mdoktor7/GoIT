from datetime import datetime, timedelta


def get_upcoming_birthdays(users):   
    # Поточна дата
    today = datetime.today().date()
    # Список майбутніх днів народження
    upcoming_birthdays = []
    # Ітерація по підготовленим користувачам
    for user in users:
        # Парсимо дату народження
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        # Заміна року на поточний для дня народження цього року
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо дата народження вже пройшла цього року
        if birthday_this_year < today:
        # Переносимо наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначаємо кі-сть днів до дня народження
        days_before_birthday = (birthday_this_year - today).days
        # Якщо день народження випадає на суботу або неділю
        if days_before_birthday <=7:
            if birthday_this_year.weekday() >= 5:
            # Знаходимо наступний понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
        # Додаємо дані про майбутній день народження
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smak", "birthday": "1990.03.16"},
    {"name": "June Smit", "birthday": "1990.03.27"},
    {"name": "Jane Wither", "birthday": "1990.03.17"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)