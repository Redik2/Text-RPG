import pyautogui
import curses
import random
from time import sleep
from src.screen import Screen
from vec2 import Vec2

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

    def run(self):
        self.screen.setup()

        self.running = True
        while self.running:
            self.update()
            self.draw()
            #sleep(1 / self.fps)
            
        self.exit()

    def update(self):
        print("update")

    def draw(self):
        #self.screen.clear()
        
        self.screen.set_text(Vec2(random.randint(0, self.screen.width - 2) // 2 * 2, random.randint(0, self.screen.height - 2) + 1), 'o')

        #self.screen.refresh()
    
    def exit(self):
        curses.endwin()