from functools import wraps


def input_error(func):
    """
    Decorator that catches common input errors
    and returns user-friendly messages.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as error:
            return str(error)

        except KeyError:
            return "Item not found."

        except IndexError:
            return "Enter required arguments."

    return inner


def parse_input(user_input: str):
    """
    Parse user input into command and arguments.
    Supports one-word and multi-word commands.
    """

    parts = user_input.strip().split()

    if not parts:
        return "", []

    two_word_commands = {
        "delete contact",
        "add birthday",
        "show birthday",
        "add email",
        "show email",
        "add note",
        "edit note",
        "delete note",
        "show notes",
        "find note",
        "add tag",
        "find tag",
        "sort notes",
    }

    if len(parts) >= 2:
        possible_command = f"{parts[0].lower()} {parts[1].lower()}"
        if possible_command in two_word_commands:
            return possible_command, parts[2:]

    return parts[0].lower(), parts[1:]