from src.objects.button import Button
from src.objects.text import Text
from src.objects.abstract_object import AbstractObject
from vec2 import Vec2
from src.screen import Screen
from src.controller import Controller

class ButtonsChoice(AbstractObject):
    def __init__(self, pos: Vec2, spacing: int = 0, type: str = "v", align: str = "top-left"):
        """
        Args:
            type (str): "v" - vertical, "h" - horizontal
        """
        super().__init__(pos, align)
        self.type = type
        self.spacing = spacing
        self.buttons: list[Button] = []
        self.selected_button = 0
    
    def add_button(self, button: Button):
        if len(self.buttons):
            button.pos = self.buttons[-1].pos + (self.buttons[-1].size + Vec2(self.spacing, self.spacing)) * Vec2(int(self.type == "h"), int(self.type == "v"))
        self.buttons.append(button)
        return super().add_child(button)

    def width(self):
        if self.type == "v":
            return max(obj.width() for obj in self.buttons)
        else:
            return sum(obj.width() for obj in self.buttons) + self.spacing * len(self.buttons)

    def height(self):
        if self.type == "v":
            return sum(obj.height() for obj in self.buttons) + self.spacing * len(self.buttons)
        else:
            return max(obj.height() for obj in self.buttons)

    def draw(self, screen: Screen, debug: bool = False):
        super().draw(screen, debug)
    
    def update(self):
        super().update()
        for i in range(len(self.buttons)):
            self.buttons[i].selected = i == self.selected_button
        
        axis = Controller.get_vector_change()
        move = axis.x if self.type == "h" else axis.y
        self.selected_button = (self.selected_button + move) % len(self.buttons)