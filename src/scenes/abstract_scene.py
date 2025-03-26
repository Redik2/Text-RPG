from abc import abstractmethod, ABC
from objects.abstract_object import AbstractObject
from vec2 import Vec2

class AbstractScene(AbstractObject, ABC):
    def __init__(self):
        super().__init__(Vec2(0, 0))
    
    @abstractmethod
    def update(self) -> str | None:
        return None