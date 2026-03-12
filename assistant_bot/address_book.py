from collections import UserDict
from datetime import date, datetime, timedelta


class Field:
    """Base class for record fields."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Class for storing a contact name."""


class Phone(Field):
    """Class for storing a phone number with validation."""

    def __init__(self, value: str) -> None:
        if not value.isdigit() or len(value) != 10:
            raise ValueError(
                "Phone number must contain exactly 10 digits."
            )
        super().__init__(value)


class Birthday(Field):
    """Class for storing a birthday in DD.MM.YYYY format."""

    def __init__(self, value: str) -> None:
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError as error:
            raise ValueError(
                "Invalid date format. Use DD.MM.YYYY"
            ) from error
        super().__init__(value)


class Record:
    """Class for storing contact information."""

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str) -> None:
        """Add a phone number to the contact."""
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str) -> Phone | None:
        """Find a phone number in the contact."""
        for item in self.phones:
            if item.value == phone:
                return item
        return None

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Replace an existing phone number with a new one."""
        phone = self.find_phone(old_phone)
        if phone is None:
            raise ValueError("Phone number not found.")
        self.phones.remove(phone)
        self.phones.append(Phone(new_phone))

    def remove_phone(self, phone: str) -> None:
        """Remove a phone number from the contact."""
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove is None:
            raise ValueError("Phone number not found.")
        self.phones.remove(phone_to_remove)

    def add_birthday(self, birthday: str) -> None:
        """Add a birthday to the contact."""
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        phones_str = "; ".join(phone.value for phone in self.phones)
        birthday_str = self.birthday.value if self.birthday else "not set"
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones_str}, "
            f"birthday: {birthday_str}"
        )


class AddressBook(UserDict):
    """Class for storing and managing contact records."""

    def add_record(self, record: Record) -> None:
        """Add a record to the address book."""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Find a record by name."""
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """Delete a record by name."""
        if name in self.data:
            del self.data[name]

    @staticmethod
    def _get_birthday_for_year(birthday: date, year: int) -> date:
        """Return birthday date for a given year."""
        try:
            return birthday.replace(year=year)
        except ValueError:
            return date(year, 3, 1)

    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        """Return birthdays for the next 7 days."""
        today = datetime.today().date()
        end_date = today + timedelta(days=7)
        result: list[dict[str, str]] = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday_date = record.birthday.date
            birthday_this_year = self._get_birthday_for_year(
                birthday_date,
                today.year,
            )

            if birthday_this_year < today:
                birthday_this_year = self._get_birthday_for_year(
                    birthday_date,
                    today.year + 1,
                )

            if today <= birthday_this_year <= end_date:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                result.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime(
                            "%d.%m.%Y"
                        ),
                    }
                )

        return result