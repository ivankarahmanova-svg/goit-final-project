from assistant_bot.handlers import (
    add_birthday,
    add_contact,
    add_note,
    add_tag,
    birthdays,
    change_contact,
    delete_contact,
    delete_note,
    edit_note,
    find_by_tag,
    find_note,
    show_all_contacts,
    show_birthday,
    show_notes,
    show_phone,
)
from assistant_bot.storage import load_data, save_data
from assistant_bot.utils import parse_input, show_help


def main() -> None:
    """Run the CLI assistant bot."""
    address_book, notes_book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(address_book, notes_book)
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(show_help())
        elif command == "add-contact":
            print(add_contact(args, address_book))
        elif command == "change-contact":
            print(change_contact(args, address_book))
        elif command == "phone":
            print(show_phone(args, address_book))
        elif command == "all-contacts":
            print(show_all_contacts(args, address_book))
        elif command == "delete-contact":
            print(delete_contact(args, address_book))
        elif command == "add-birthday":
            print(add_birthday(args, address_book))
        elif command == "show-birthday":
            print(show_birthday(args, address_book))
        elif command == "birthdays":
            print(birthdays(args, address_book))
        elif command == "add-note":
            print(add_note(args, notes_book))
        elif command == "edit-note":
            print(edit_note(args, notes_book))
        elif command == "delete-note":
            print(delete_note(args, notes_book))
        elif command == "show-notes":
            print(show_notes(args, notes_book))
        elif command == "find-note":
            print(find_note(args, notes_book))
        elif command == "add-tag":
            print(add_tag(args, notes_book))
        elif command == "find-tag":
            print(find_by_tag(args, notes_book))
        else:
            print("Invalid command. Type 'help' to see commands.")


if __name__ == "__main__":
    main()