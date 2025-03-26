from abc import abstractmethod, ABC
from src.objects.abstract_object import AbstractObject
from vec2 import Vec2

class AbstractScene(AbstractObject, ABC):
    def __init__(self, size: Vec2):
        super().__init__(Vec2(0, 0))
        self.size = size
    
    @abstractmethod
    def update(self) -> str | None:
        super().update()
        return None
    
    def width(self):
        return self.size.x
    
    def height(self):
        return self.size.y