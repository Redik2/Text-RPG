from .abstract_scene import AbstractScene
from src.objects.button import Button
from src.objects.text import Text
from src.objects.buttons_choice import ButtonsChoice
from vec2 import Vec2
from src.controller import Controller

class Menu(AbstractScene):
    def __init__(self, size: Vec2):
        super().__init__(size)
        self.buttons = self.add_child(ButtonsChoice(self.size / 2, 0, "v", "mid-mid"))
        self.buttons.add_button(Button(Vec2(0, 0), Vec2(20, 5), "Play"))
        self.buttons.add_button(Button(Vec2(0, 0), Vec2(20, 5), "Settings"))
        self.buttons.add_button(Button(Vec2(0, 0), Vec2(20, 5), "Exit"))
        self.pressed = self.add_child(Text(Vec2(1, 1), "Menu"))
    
    def update(self):
        super().update()
        if Controller.is_confirmed():
            return ["game", "settings", "exit"].__getitem__(self.buttons.selected_button)

    
    def draw(self, screen, debug = False):
        super().draw(screen, debug)
