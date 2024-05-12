from collections import UserDict
from datetime import datetime, timedelta
import pickle
from pathlib import Path
from abc import ABC, abstractmethod


filename = Path("data/database.bin")


class Interface(ABC):
    @abstractmethod
    def send_message(self, message):
        pass


class ConsoleInterface(Interface):
    def send_message(self, message):
        print(message)


class WebInterface(Interface):
    def send_message(self, message):
        print(f"FAKE_WEB {message}")


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) == 10 and value.isdigit():
            self.__value = value
        else:
            raise ValueError("Phone number must be 10 digits.")


class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Birthday must have format day.month.year")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))   

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if str(phone) == old_number:
                phone.value = new_number
                return
        raise ValueError("Phone number not found")

    def add_birthday(self, birthday):
        if self.birthday is None:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Only one birthday can be added.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    @staticmethod
    def find_next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:  
            days_ahead += 7
        return d + timedelta(days_ahead)

    def get_upcoming_birthdays(self, days=7) -> list:
        today = datetime.today().date()
        upcoming_birthdays = []

        for user in self.data.values():
            if user.birthday is None:
                continue
            birthday_this_year = user.birthday.date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday() >= 5:  # субота або неділя
                    birthday_this_year = self.find_next_weekday(
                        birthday_this_year, 0
                    )  

                congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
                upcoming_birthdays.append(
                    {
                        "name": user.name.value,
                        "congratulation_date": congratulation_date_str,
                    }
                )

        return upcoming_birthdays


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please." 
        except KeyError:
            return "Contact not found."
        except IndexError:    
            return "Invalid command format."
    return inner 


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise KeyError 


@input_error
def show_contact(args, book):
    (name,) = args
    record = book.find(name)
    if record:
        return "; ".join([str(phone) for phone in record.phones])
    else:
        raise KeyError
    

@input_error
def delete_contact(args, book: AddressBook):
    name = args[0]
    if name in book:
        del book[name]
        return f"Contact '{name}' deleted successfully."
    else:
        raise KeyError("Contact not found.")


@input_error
def show_all(book):
    # return "\n".join([str(record) for record in book.data.values()])
    for name, record in book.items():
        phones = "; ".join(str(phone) for phone in record.phones)
        print(f"{name}: {phones}")
    if not book:
        return "No contacts found."


@input_error
def add_birthday(args, book: AddressBook):
    name = args[0]
    birthday = args[1]
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday was added."
    else:
        raise KeyError
  

@input_error
def show_birthday(args, book):
    (name,) = args
    record = book.find(name)
    return str(record.birthday)


@input_error
def all_birthdays(args, book: AddressBook):
    birthdays_exist = False
    for name, record in book.items():
        if record.birthday:
            print(f"{name}: {record.birthday}")
            birthdays_exist = True
    
    if not birthdays_exist:
        return "No birthdays found."


def save_data(book):
        with open(filename, "wb") as f:
            pickle.dump(book, f)


def load_data():
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()    



@input_error
def main():
    book = load_data()
    ui = WebInterface()

    ui.send_message("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command:")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "q"]:
            ui.send_message("Good bye!")
            save_data(book)
            return False

        elif command == "add":
            ui.send_message(add_contact(args, book))

        elif command == "change":
            ui.send_message(change_contact(args, book))

        elif command == "delete":
            ui.send_message(delete_contact(args, book))

        elif command == "show":
            ui.send_message(show_contact(args, book))

        elif command == "all":
            ui.send_message(show_all(book))

        elif command == "hello":
            ui.send_message("How can I help you?")
       
        elif command == "add-birthday":
            ui.send_message(add_birthday(args, book))
        
        elif command == "show-birthday":
            ui.send_message(show_birthday(args, book))

        elif command == "all-birthdays":
            ui.send_message(all_birthdays(args, book))

        elif command == "birthdays":
            birthdays = book.get_upcoming_birthdays()
            if not len(birthdays):
                ui.send_message("There are no upcoming birthdays.")
                continue
            for day in birthdays:
                ui.send_message(f"{day}")

        else:
            ui.send_message("Invalid command.")
        

if __name__ == "__main__":
    main()
