import keyboard
from vec2 import Vec2
import msvcrt

class Controller:
    """Класс для обработки нажатий клавиш с защитой от дребезга (перелетов)."""

    last_state = {"w": False, "s": False, "a": False, "d": False}
    pressed_per_frame: list[bytes] = []
    confirm_keys = [b' ', b'\r']


    @staticmethod
    def update_frame_pressed():
        Controller.pressed_per_frame.clear()
        while msvcrt.kbhit():
            Controller.pressed_per_frame.append(msvcrt.getch())

    @staticmethod
    def is_pressed(button: bytes) -> bool:
        """Проверяет, нажата ли клавиша прямо сейчас."""
        return button in Controller.pressed_per_frame

    @staticmethod
    def get_vector_change() -> Vec2:
        """
        Возвращает вектор направления движения (WASD + стрелки),  
        но учитывает только изменения (нажатие впервые).
        """
        keys = {
            "left": Controller.is_pressed(b'a'),
            "right": Controller.is_pressed(b'd'),
            "up": Controller.is_pressed(b'w'),
            "down": Controller.is_pressed(b's'),
        }

        x = int(keys["right"] and not Controller.last_state["right"]) - int(keys["left"] and not Controller.last_state["left"])
        y = int(keys["down"] and not Controller.last_state["down"]) - int(keys["up"] and not Controller.last_state["up"])

        Controller.last_state = keys  # Обновляем состояние

        return Vec2(x, y)

    @staticmethod
    def get_vector() -> Vec2:
        """
        Возвращает вектор направления движения на основе нажатых клавиш (WASD и стрелки).
        
        :return: Vec2(x, y), где x и y могут быть -1, 0 или 1.
        """
        x = (Controller.is_pressed(b"d")) - \
            (Controller.is_pressed(b"a"))

        y = (Controller.is_pressed(b"s")) - \
            (Controller.is_pressed(b"w"))

        return Vec2(x, y)

    def is_confirmed() -> bool:
        return any(Controller.is_pressed(key) for key in Controller.confirm_keys)