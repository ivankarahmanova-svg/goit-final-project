import pickle
from assistant_bot.address_book import AddressBook
from assistant_bot.notes import NotesBook


def save_data(address_book: AddressBook, notes_book: NotesBook,
              filename: str = "data.bin") -> None:
    """
    Save contacts and notes to file using pickle serialization.
    """

    # Open file in binary write mode
    with open(filename, "wb") as file:

        # Serialize objects and write them to file
        pickle.dump(
            {
                "contacts": address_book,
                "notes": notes_book,
            },
            file,
        )


def load_data(filename: str = "data.bin"):
    """
    Load saved data from file.
    If file does not exist, create empty AddressBook and NotesBook.
    """

    try:
        # Open file in binary read mode
        with open(filename, "rb") as file:
            data = pickle.load(file)

            return data["contacts"], data["notes"]

    except FileNotFoundError:
        # If file does not exist return empty objects
        return AddressBook(), NotesBook()