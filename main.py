from assistant_bot.storage import load_data, save_data
from assistant_bot.utils import parse_input


def main():
    """
    Main function that starts CLI assistant.
    """

    # Load saved contacts and notes from file
    address_book, notes_book = load_data()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ")

        # Parse user input
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Save all data before exiting program
            save_data(address_book, notes_book)

            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()