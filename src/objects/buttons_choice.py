from src.objects.button import Button
from src.objects.text import Text
from src.objects.abstract_object import AbstractObject
from vec2 import Vec2

class ButtonsChoice(AbstractObject):
    def __init__(self, pos: Vec2, spacing: int = 0, type: str = "v"):
        """
        Args:
            type (str): "v" - vertical, "h" - horizontal
        """
        super().__init__(pos)
        self.type = type
        self.spacing = spacing
        self.buttons: list[Button] = []
    
    def add_button(self, button: Button):
        if len(self.buttons):
            button.pos = self.buttons[-1].pos + (self.buttons[-1].size + Vec2(self.spacing, self.spacing)) * Vec2(int(self.type == "h"), int(self.type == "v"))
        self.buttons.append(button)
        return super().add_child(button)
