from abc import ABC


class Obj(ABC):
    def __init__(self, x: int, y: int):
        super().__init__()