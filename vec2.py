import math

class Vec2:
    """Класс двумерного вектора с перегруженными операциями."""

    def __init__(self, x: float, y: float):
        """Конструктор, инициализирующий координаты вектора."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Перегруженный оператор сложения (+) для векторов и кортежей."""
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vec2(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Vec2 can be add only to Vec2(x, y), Tuple(x, y)")

    def __sub__(self, other):
        """Перегруженный оператор вычитания (-) для векторов и кортежей."""
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vec2(self.x - other[0], self.y - other[1])
        else:
            raise TypeError("Vec2 can be add only to Vec2(x, y), Tuple(x, y)")

    def __mul__(self, other):
        """Перегруженный оператор умножения (*) для векторов и чисел."""
        if isinstance(other, (int, float)):
            return Vec2(self.x * other, self.y * other)
        elif isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vec2(self.x * other[0], self.y * other[1])
        else:
            raise TypeError("Vec2 can be multiplied only by a number, Vec2(x, y), or Tuple(x, y)")

    def __truediv__(self, other):
        """Перегруженный оператор деления (/) для векторов и чисел."""
        if isinstance(other, (int, float)):
            return Vec2(self.x / other, self.y / other)
        elif isinstance(other, Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vec2(self.x / other[0], self.y / other[1])
        else:
            raise TypeError("Vec2 can be divided only by a number, Vec2(x, y), or Tuple(x, y)")

    def length(self) -> float:
        """Возвращает длину (модуль) вектора."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        """Возвращает нормализованный вектор (единичной длины)."""
        l = self.length()
        return Vec2(self.x / l, self.y / l) if l != 0 else Vec2(0, 0)

    def tuple(self) -> tuple:
        """Возвращает вектор в виде кортежа (x, y)."""
        return self.x, self.y

    def __str__(self):
        """Возвращает строковое представление вектора."""
        return f"({self.x}, {self.y})"
    
    def copy(self):
        """Возвращает новый класс с теми же значениями"""
        return Vec2(self.x, self.y)