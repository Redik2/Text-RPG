import pyautogui
import curses
import random
from time import sleep
from src.screen import Screen
from vec2 import Vec2
import math

def zoom_in():
    pyautogui.hotkey("ctrl", "+")

def zoom_out():
    pyautogui.hotkey("ctrl", "-")


class Application:
    def __init__(self, w: int, h: int, fps: int, zoom_out: int):
        self.fps = fps
        self.zoom_out = zoom_out
        self.running = False
        self.screen = Screen(w, h)
        self.scenes = {}

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()
            sleep(1 / self.fps)
            
        self.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.clear()

        pos1 = Vec2(random.randint(0, 50), random.randint(0, 30))
        size = Vec2(random.randint(3, 20), random.randint(3, 20))
        self.screen.draw_box(pos1, pos1 + size, random.randint(0, 2))

        self.screen.refresh()
    
    def exit(self):
        curses.endwin()