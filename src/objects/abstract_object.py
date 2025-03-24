from abc import ABC, abstractmethod
from vec2 import Vec2
import curses


class AbstractObject(ABC):
    def __init__(self, pos: Vec2):
        self.pos = pos
        self.parent: AbstractObject | None = None
        self.children: list[AbstractObject] = []
    
    def update(self) -> None:
        for child in self.children:
            child.update()

    def draw(self, screen: curses.window) -> None:
        for child in self.children:
            child.draw()

    def gpos(self) -> Vec2:
        if not self.parent:
            return self.pos
        return self.pos + self.parent.gpos()