import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and 0 < quantity <= max - min + 1:
        numbers_ticket = set()
        while len(numbers_ticket) < quantity:
            numbers_ticket.add(random.randint(min, max))
        return sorted(list(numbers_ticket))
    else:
        return []

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Your loterry numbers: {lottery_numbers}")