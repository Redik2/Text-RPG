from src.objects.abstract_object import AbstractObject
from src.objects.text import Text
from vec2 import Vec2
from src.screen import Screen, get_mouse_state

class Button(AbstractObject):
    def __init__(self, pos: Vec2, size: Vec2):
        super().__init__(pos)
        self.size = size
        self.selected = False

        self.add_child(Text(self.pos + Vec2(1, 1), "test"))
    
    def draw(self, screen: Screen):
        super().draw(screen)
        screen.draw_box(self.gpos(), self.gpos() + self.size, int(self.selected))
    
    def update(self) -> bool:
        mouse_data = get_mouse_state()
        self.children[-1].text = str(mouse_data)
        if not mouse_data:
            return False

        mx, my, clicked = mouse_data
        x1, y1 = self.pos.x, self.pos.y
        x2, y2 = self.pos.x + self.size.x, self.pos.y + self.size.y

        # Проверяем, находится ли курсор внутри границ кнопки
        if x1 <= mx < x2 and y1 <= my < y2:
            self.selected = True
            if clicked:
                return True  # Кнопка нажата
        else:
            self.selected = False

        return False