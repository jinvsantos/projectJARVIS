import os


def clean() -> None:
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("clear")
