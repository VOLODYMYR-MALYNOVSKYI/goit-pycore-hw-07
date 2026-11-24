# Завдання

# Декоратор для обробки помилок

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e) if str(e) else "Give me name and phone please."
        except KeyError as e:
            return str(e).strip("'") if str(e) else "Contact not found."
        except IndexError as e:
            return str(e) if str(e) else "Enter user name."

    return inner

# Допоміжні функції

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    name_lower = name.lower()
    if name_lower in contacts:
        return "Error: contact already exists."

    contacts[name_lower] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    name_lower = name.lower()
    if name_lower not in contacts:
        raise KeyError
    contacts[name_lower] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0].lower()
    if name not in contacts:
        raise KeyError
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "Error: no contacts found."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

# Головна функція для взаємодії з користувачем

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()