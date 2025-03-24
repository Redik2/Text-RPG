import curses
from vec2 import Vec2

class Screen:
    def __init__(self, w: int, h: int):
        self.stdscr = None
        self.width = w * 2
        self.height = h
    
    def setup(self):
        self.stdscr = curses.initscr()
        curses.curs_set(0)
        self.stdscr.resize(self.height, self.width)

    def clear(self):
        self.stdscr.clear()
    
    def refresh(self):
        self.stdscr.refresh()
    
    def set_text(self, pos: Vec2, character: str):
        try:
            self.stdscr.addch(pos.y, pos.x * 2, character)
        except curses.error:
            return