from colorama import init, Fore, Back, Style
init()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please." 
        except KeyError:
            return Fore.RED + "Contact not found." + Style.RESET_ALL
        except IndexError:    
            return Fore.RED + "Invalid comand format."+ Style.RESET_ALL
    return inner 


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts): 
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated successfully" 

@input_error
def show_contact(args, contacts):
    name = args[0]
    return Fore.GREEN + contacts[name] + Style.RESET_ALL
    

@input_error
def show_all_contacts(args, contacts):
    for name, phone in contacts.items():
        print(Fore.GREEN + f"{name}: {phone}" + Style.RESET_ALL)
    if not contacts:
        return Back.RED + "No contacts found." + Style.RESET_ALL

@input_error
def main():
    contacts = {}
    print(Back.BLUE + Fore.YELLOW + "Welcome to the assistant bot!" + Style.RESET_ALL)
    while True:
        user_input = input(Fore.GREEN + "Enter a command:" + Style.RESET_ALL)
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Back.BLUE + Fore.YELLOW + "Good bye!" + Style.RESET_ALL)
            return False

        elif command == "add":
            print (Back.BLUE + Fore.YELLOW + add_contact(args, contacts) + Style.RESET_ALL) 

        elif command == "change":
            print(Back.BLUE + Fore.YELLOW + change_contact(args, contacts) + Style.RESET_ALL)

        elif command == "show":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all_contacts(args, contacts))

        elif command == "hello":
            print(Back.BLUE + Fore.YELLOW + "How can I help you?" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid command." + Style.RESET_ALL)
        


if __name__ == "__main__":
    main()
