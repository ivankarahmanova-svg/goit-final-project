from collections import UserDict
from datetime import datetime


class Field:
    """Base class for all fields."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Class for storing contact name."""


class Phone(Field):
    """Class for storing phone numbers."""

    def __init__(self, value: str) -> None:
        # Validate phone number (must contain exactly 10 digits)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    """Class for storing birthday."""

    def __init__(self, value: str) -> None:
        try:
            # Convert string date to datetime object
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)


class Email(Field):
    """Class for storing email."""

    def __init__(self, value: str) -> None:
        # Basic email validation
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format.")
        super().__init__(value)


class Record:
    """Class for storing contact information."""

    def __init__(self, name: str) -> None:
        # Contact name
        self.name = Name(name)

        # List of phone numbers
        self.phones = []

        # Optional fields
        self.birthday = None
        self.email = None

    def add_phone(self, phone: str) -> None:
        """Add phone number to contact."""
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str):
        """Find phone number in contact."""
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit existing phone number."""
        phone = self.find_phone(old_phone)
        if phone is None:
            raise ValueError("Phone not found.")
        self.phones.remove(phone)
        self.phones.append(Phone(new_phone))

    def add_birthday(self, birthday: str) -> None:
        """Add birthday to contact."""
        self.birthday = Birthday(birthday)

    def add_email(self, email: str) -> None:
        """Add email to contact."""
        self.email = Email(email)

    def __str__(self) -> str:
        phones = "; ".join(phone.value for phone in self.phones)
        birthday = self.birthday.value if self.birthday else "not set"
        email = self.email.value if self.email else "not set"

        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}, "
            f"birthday: {birthday}, "
            f"email: {email}"
        )


from datetime import datetime, timedelta

class AddressBook(UserDict):
    """Class for managing contacts."""

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():

            if record.birthday is None:
                continue

            birthday = record.birthday.value
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta = (birthday_this_year - today).days

            if delta <= 7:
                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")
                })

        return upcoming