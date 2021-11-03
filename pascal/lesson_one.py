from introductie import app


def get_pascal() -> int:
    for i in range(11):
        if app.say_hello_from_name(i).casefold().endswith("pascal"):
            return i


def get_pascal_one_line() -> int:
    return next(
        i for i in range(11) if app.say_hello_from_name(i).casefold().endswith("pascal")
    )
