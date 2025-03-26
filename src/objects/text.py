from src.objects.abstract_object import AbstractObject
from vec2 import Vec2
from src.screen import Screen

class Text(AbstractObject):
    def __init__(self, pos: Vec2, text: str):
        super().__init__(pos)
        self.text = text
    
    def draw(self, screen: Screen):
        super().draw(screen)
        pos = self.gpos()
        for ch in self.text:
            screen.set_char(pos, ch)
            pos.x += 0.5

            if ch == "\n":
                pos.x = self.gpos().x
                pos.y += 1