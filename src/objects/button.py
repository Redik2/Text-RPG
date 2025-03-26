from src.objects.abstract_object import AbstractObject
from src.objects.text import Text
from vec2 import Vec2
from src.screen import Screen

class Button(AbstractObject):
    def __init__(self, pos: Vec2, size: Vec2):
        super().__init__(pos)
        self.size = size - Vec2(1, 1)
        self.selected = False

        self.text_element = self.add_child(Text(self.pos + self.size / 2, "test"))
    
    def draw(self, screen: Screen):
        super().draw(screen)
        screen.draw_box(self.gpos(), self.gpos() + self.size, int(self.selected))
    
    def update(self):
        super().update()
        self.text_element.text = str(self.text_element.gpos())