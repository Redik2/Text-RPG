from .abstract_scene import AbstractScene
from src.objects.button import Button
from src.objects.text import Text
from src.objects.buttons_choice import ButtonsChoice
from vec2 import Vec2

class Menu(AbstractScene):
    def __init__(self):
        super().__init__()
        buttons = self.add_child(ButtonsChoice(Vec2(10, 10)))
        buttons.add_button(Button(Vec2(0, 0), Vec2(20, 5)))
        buttons.add_button(Button(Vec2(0, 0), Vec2(20, 5)))
        buttons.add_button(Button(Vec2(0, 0), Vec2(20, 5)))
        self.add_child(Text(Vec2(1, 1), "Menu"))
    
    def update(self):
        super().update()