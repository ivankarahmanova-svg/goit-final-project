from assistant_bot.address_book import AddressBook, Record
from assistant_bot.notes import Note, NotesBook
from assistant_bot.utils import input_error


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    name, phone = args
    record = book.find(name)

    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."

    record.add_phone(phone)
    return "Phone added to existing contact."


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError

    return "; ".join(phone.value for phone in record.phones)


@input_error
def show_all_contacts(args: list[str], book: AddressBook) -> str:
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def delete_contact(args: list[str], book: AddressBook) -> str:
    name = args[0]

    if book.find(name) is None:
        raise KeyError

    book.delete(name)
    return "Contact deleted."


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        return "Birthday not set."

    return record.birthday.value


@input_error
def birthdays(args: list[str], book: AddressBook) -> str:
    result = book.get_upcoming_birthdays()

    if not result:
        return "No birthdays in the next week."

    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}"
        for item in result
    )


@input_error
def add_note(args: list[str], notes_book: NotesBook) -> str:
    title = args[0]
    content = " ".join(args[1:])

    if not content:
        return "Enter note content."

    note = Note(title, content)
    notes_book.add_note(note)
    return "Note added."


@input_error
def edit_note(args: list[str], notes_book: NotesBook) -> str:
    title = args[0]
    new_content = " ".join(args[1:])

    note = notes_book.find_by_title(title)
    if note is None:
        raise KeyError

    note.edit_content(new_content)
    return "Note updated."


@input_error
def delete_note(args: list[str], notes_book: NotesBook) -> str:
    title = args[0]

    if not notes_book.delete_note(title):
        raise KeyError

    return "Note deleted."


@input_error
def show_notes(args: list[str], notes_book: NotesBook) -> str:
    return notes_book.show_all()


@input_error
def find_note(args: list[str], notes_book: NotesBook) -> str:
    title = args[0]
    note = notes_book.find_by_title(title)

    if note is None:
        raise KeyError

    return str(note)


@input_error
def add_tag(args: list[str], notes_book: NotesBook) -> str:
    title, tag = args
    note = notes_book.find_by_title(title)

    if note is None:
        raise KeyError

    note.add_tag(tag)
    return "Tag added."


@input_error
def find_by_tag(args: list[str], notes_book: NotesBook) -> str:
    tag = args[0]
    found_notes = notes_book.find_by_tag(tag)

    if not found_notes:
        return "No notes with this tag."

    return "\n".join(str(note) for note in found_notes)
@input_error
def add_email(args: list[str], book: AddressBook) -> str:
    name, email = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_email(email)
    return "Email added."


@input_error
def show_email(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError

    if record.email is None:
        return "Email not set."

    return record.email.value