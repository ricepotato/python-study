from datetime import datetime
from typing import Callable


def greet(name: str, greeting_intro: str) -> str:
    return f"{greeting_intro}, {name}"


def greet_list(names: list[str], greeting_intro: str) -> list[str]:
    return [greet(name, greeting_intro) for name in names]


def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def main() -> None:
    name = "ricepotato"
    greeting_intro = read_greeting()

    print(greet(name, greeting_intro))
    print(greet_list(["John", "Jane", "Joe"], greeting_intro))


if __name__ == "__main__":
    main()
