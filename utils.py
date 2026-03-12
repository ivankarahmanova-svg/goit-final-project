def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError:
            return "Invalid input."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter command correctly."
    return wrapper