def parse_input(user_input: str) -> tuple[str, ...]:
    """Parse user input into a command and its arguments."""
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except ValueError:
        return ("Invalid",)


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Update a contact's phone number using an exact name match."""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found"


def find_contacts(name: str, contacts: dict[str, str]) -> list[tuple[str, str]]:
    """Find all contacts matching a name, ignoring case."""
    matches = []
    for stored_name, phone in contacts.items():
        if stored_name.casefold() == name.casefold():
            matches.append((stored_name, phone))
    return matches


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Return the phone number for a single match or formatted
    contact details when multiple names match.
    """
    name = args[0]
    matches = find_contacts(name, contacts)

    if not matches:
        return "Phone not found"

    if len(matches) == 1:
        return matches[0][1]

    return "\n".join(f"{name}: {phone}" for name, phone in matches)


def show_all(contacts: dict[str, str]) -> str:
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        try:
            if command in ["exit", "close"]:
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
        except (ValueError, IndexError):
            print("Invalid command.")


if __name__ == "__main__":
    main()
