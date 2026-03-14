from functools import wraps


# Decorator for handling user input errors
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
    """

    parts = user_input.strip().split()

    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args