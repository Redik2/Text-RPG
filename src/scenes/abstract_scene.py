from objects.abstract_object import AbstractObject
from vec2 import Vec2

class AbstractScene(AbstractObject):
    def __init__(self):
        super().__init__(Vec2(0, 0))