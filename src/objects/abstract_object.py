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
            child.draw(screen)

    def gpos(self) -> Vec2:
        if not self.parent:
            return self.pos
        return self.pos + self.parent.gpos()
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        return child
    
    def set_parent(self, new_parent):
        self.parent.children.remove(self)
        new_parent.add_child(self)