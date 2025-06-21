# Input.py

# (c) Jobe, 2025


import sys
import keyboard



__all__ = [
    "input"
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
