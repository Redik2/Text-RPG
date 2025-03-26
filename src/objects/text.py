from src.objects.abstract_object import AbstractObject
from vec2 import Vec2
from src.screen import Screen

class Text(AbstractObject):
    def __init__(self, pos: Vec2, text: str, align: str = "top-left"):
        super().__init__(pos, align)
        self.text = text
    
    def width(self):
        return max(list(map(len, self.text.split("\n")))) / 2
    
    def height(self):
        return self.text.count("\n") + 1

    def draw(self, screen: Screen, debug: bool = False):
        super().draw(screen, debug)
        pos = self.gpos()
        for ch in self.text:
            screen.set_char(pos, ch)
            pos.x += 0.5

            if ch == "\n":
                pos.x = self.gpos().x
                pos.y += 1