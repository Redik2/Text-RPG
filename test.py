import msvcrt
from time import sleep

while True:
    was_pressed = ""
    while msvcrt.kbhit():
        was_pressed += str(msvcrt.getch()) + ' '
    if was_pressed:
        print(was_pressed)