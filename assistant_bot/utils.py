from collections.abc import Callable
from functools import wraps


def input_error(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError:
            return "Item not found."
        except IndexError:
            return "Enter the required arguments."

    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def show_help() -> str:
    return (
        "Available commands:\n"
        "hello\n"
        "help\n"
        "add-contact <name> <phone>\n"
        "change-contact <name> <old_phone> <new_phone>\n"
        "phone <name>\n"
        "all-contacts\n"
        "delete-contact <name>\n"
        "add-birthday <name> <DD.MM.YYYY>\n"
        "show-birthday <name>\n"
        "birthdays\n"
        "add-note <title> <content>\n"
        "edit-note <title> <new content>\n"
        "delete-note <title>\n"
        "show-notes\n"
        "find-note <title>\n"
        "add-tag <title> <tag>\n"
        "find-tag <tag>\n"
        "close\n"
        "exit"
    )