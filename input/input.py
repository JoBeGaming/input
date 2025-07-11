# Input.py

# (c) Jobe, 2025


import sys
import keyboard

from typing import Any



__all__ = [
    "input",
    "KeyboardStdInObject",
]


def input(msg: str, /, *, file: ... = sys.stdout) -> str:
    file.write(msg)
    res = ""
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == "enter":
                break
            elif key == "space":
                res += " "
                file.write(" ")
            elif key == "backspace":
                if len(res) > 0:
                    res = res[:-1]
                    file.write("\b \b")  # Erase last character
            elif len(key) == 1:
                res += key
                file.write(key)

            file.flush()
          
    return res

class KeyboardStdInObject:

    def __init__(self) -> None:
        self.res = ""
        self.__written = False

    def __str__(self) -> str:
        return self.res

    def __bool__(self) -> bool:
        return self.__written

    def __add__(self, other: Any) -> str
        self.__written = True
        if other.event_type == keyboard.KEY_DOWN:
            key = other.name

            if key == "enter":
                self.res += "\n"
            elif key == "space":
                self.res += " "
            elif key == "backspace":
                if len(self.res) > 0:
                    self.res = self.res[:-1]
            elif len(key) == 1:
                self.res += key
        return self.res

    def as_file(self) -> TextIO:
        with open("KeyboardStdInObject.dump", "w") as file:
            file.write(self.res)
        return file
