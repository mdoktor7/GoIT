from colorama import init, Fore, Back, Style
init()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Please enter name and phone number" + Style.RESET_ALL 
    name, phone = args
    contacts[name] = phone
    return Back.BLUE + Fore.YELLOW + "Contact added." + Style.RESET_ALL


def change_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Please enter name and phone number" + Style.RESET_ALL   
    name, phone = args
    if name not in contacts:
        return Fore.RED + "Contact not found." + Style.RESET_ALL
    contacts[name] = phone
    return Back.BLUE + Fore.YELLOW + "Contact updated successfully" + Style.RESET_ALL

def show_contact(args, contacts):
    if len(args) != 1:
        return Fore.RED + "Please enter a name to show the contact's phone number" + Style.RESET_ALL
    name = args[0]
    if name not in contacts:
        return Fore.RED + "Contact not found." + Style.RESET_ALL
    return Back.BLUE + Fore.YELLOW + contacts[name] + Style.RESET_ALL


def main():
    contacts = {}
    print(Back.BLUE + Fore.YELLOW + "Welcome to the assistant bot!" + Style.RESET_ALL)
    while True:
        user_input = input(Fore.GREEN + "Enter a command: " + Style.RESET_ALL)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Back.BLUE + Fore.YELLOW + "Good bye!" + Style.RESET_ALL)
            return False

        elif command == "add":
            message = add_contact(args, contacts) 
            print(Back.BLUE + Fore.YELLOW + message + Style.RESET_ALL)

        elif command == "change":
            message = change_contact(args, contacts)
            print(Back.BLUE + Fore.YELLOW + message + Style.RESET_ALL)

        elif command == "show":
            message = show_contact(args, contacts)
            print(Back.BLUE + message + Style.RESET_ALL)

        elif command == "hello":
            print(Back.BLUE + Fore.YELLOW + "How can I help you?" + Style.RESET_ALL)

        else:
            print(Fore.RED + "Invalid command." + Style.RESET_ALL)


if __name__ == "__main__":
    main()