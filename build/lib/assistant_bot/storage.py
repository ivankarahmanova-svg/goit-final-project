import pickle

from assistant_bot.address_book import AddressBook
from assistant_bot.notes import NotesBook


def save_data(
    address_book: AddressBook,
    notes_book: NotesBook,
    filename: str = "data.bin"
) -> None:
    with open(filename, "wb") as file:
        pickle.dump(
            {
                "contacts": address_book,
                "notes": notes_book,
            },
            file
        )


def load_data(filename: str = "data.bin") -> tuple[AddressBook, NotesBook]:
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
            return data["contacts"], data["notes"]
    except FileNotFoundError:
        return AddressBook(), NotesBook()