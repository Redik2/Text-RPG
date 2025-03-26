from abc import ABC, abstractmethod
from vec2 import Vec2
from src.screen import Screen


class AbstractObject(ABC):
    def __init__(self, pos: Vec2, align: str = "top-left"):
        self.pos = pos
        self.parent: AbstractObject | None = None
        self.children: list[AbstractObject] = []
        self.v_align = align.split('-')[0]
        self.h_align = align.split('-')[1]
    
    def update(self) -> None:
        for child in self.children:
            child.update()

    def draw(self, screen: Screen, debug: bool = False) -> None:
        for child in self.children:
            child.draw(screen, debug)
        if debug:
            screen.set_pixel(self.gpos())

    def gpos(self) -> Vec2:
        pos = self.pos.copy()
        match self.h_align:
            case "left":
                pass
            case "mid":
                pos.x -= self.width() / 2
            case "right":
                pos.x -= self.width()
        match self.v_align:
            case "top":
                pass
            case "mid":
                pos.y -= self.height() / 2
            case "bottom":
                pos.y -= self.height()
        if not self.parent:
            return pos
        return pos + self.parent.gpos()
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        return child
    
    def set_parent(self, new_parent):
        self.parent.children.remove(self)
        new_parent.add_child(self)
    
    @abstractmethod
    def width(self) -> float:
        return 1
    
    @abstractmethod
    def height(self) -> float:
        return 1