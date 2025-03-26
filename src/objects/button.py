from src.objects.abstract_object import AbstractObject
from src.objects.text import Text
from vec2 import Vec2
from src.screen import Screen

class Button(AbstractObject):
    def __init__(self, pos: Vec2, size: Vec2, text: str = "", align: str = "top-left"):
        super().__init__(pos, align)
        self.size = size
        self.selected = False

        self.text_element = self.add_child(Text(self.pos + Vec2(0.5, 1) + (self.size - Vec2(0, 2)) / 2, text, "mid-mid"))
    
    def draw(self, screen: Screen, debug: bool = False):
        super().draw(screen, debug)
        pos = self.gpos()
        screen.draw_box(pos, pos + self.size - Vec2(0, 1), int(self.selected))
    
    def update(self):
        super().update()
        #self.text_element.text = str(self.text_element.gpos())
    
    def width(self):
        return self.size.x

    def height(self):
        return self.size.y