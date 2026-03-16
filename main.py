from assistant_bot.storage import load_data, save_data
from assistant_bot.utils import parse_input
from assistant_bot.handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all_contacts,
    delete_contact,
    add_birthday,
    show_birthday,
    birthdays,
    add_note,
    edit_note,
    delete_note as remove_note,
    show_notes,
    find_note,
    add_tag,
    find_by_tag,
    add_email,
    show_email,
    search_contacts,
    sort_notes_by_tags,
)


def show_help() -> str:
    return """
Available commands:

Contacts:
  hello
  add <name> <phone>
  change <name> <old_phone> <new_phone>
  phone <name>
  all
  delete contact <name>
  add birthday <name> <DD.MM.YYYY>
  show birthday <name>
  birthdays
  add email <name> <email>
  show email <name>

Notes:
  add note <title> <content>
  edit note <title> <new content>
  delete note <title>
  show notes
  find note <title>
  add tag <title> <tag>
  find tag <tag>
  sort notes

General:
  help
  close / exit
""".strip()


def main():
    """
    Main function that starts CLI assistant.
    """

    address_book, notes_book = load_data()

    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")

    while True:
        user_input = input("Enter command: ").strip()

        if not user_input:
            print("Enter command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(address_book, notes_book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "help":
            print(show_help())

        elif command == "add":
            print(add_contact(args, address_book))

        elif command == "change":
            print(change_contact(args, address_book))

        elif command == "phone":
            print(show_phone(args, address_book))

        elif command == "all":
            print(show_all_contacts(args, address_book))

        elif command == "delete contact":
            print(delete_contact(args, address_book))

        elif command == "add birthday":
            print(add_birthday(args, address_book))

        elif command == "show birthday":
            print(show_birthday(args, address_book))

        elif command == "birthdays":
            print(birthdays(args, address_book))

        elif command == "add email":
            print(add_email(args, address_book))

        elif command == "show email":
            print(show_email(args, address_book))

        elif command == "add note":
            print(add_note(args, notes_book))

        elif command == "edit note":
            print(edit_note(args, notes_book))

        elif command == "delete note":
            print(remove_note(args, notes_book))

        elif command == "show notes":
            print(show_notes(args, notes_book))

        elif command == "find note":
            print(find_note(args, notes_book))

        elif command == "add tag":
            print(add_tag(args, notes_book))

        elif command == "find tag":
            print(find_by_tag(args, notes_book))
        elif command == "search":
            print(search_contacts(args, address_book))
        elif command == "sort notes":
            print(sort_notes_by_tags(args, notes_book))
        else:
            print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()