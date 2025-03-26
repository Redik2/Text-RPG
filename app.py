import pyautogui
import curses
import random
from time import sleep
from src.screen import Screen
from vec2 import Vec2
from src.scenes.menu import Menu

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

        self.scenes = {"menu": Menu()}
        self.active_scene = "menu"

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()
            sleep(1 / self.fps)
            
        self.exit()

    def update(self):
        self.scenes[self.active_scene].update()

    def draw(self):
        self.screen.clear()

        self.scenes[self.active_scene].draw(self.screen)

        self.screen.refresh()
    
    def exit(self):
        curses.endwin()