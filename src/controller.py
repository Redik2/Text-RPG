import keyboard
from vec2 import Vec2

class Controller:
    """Класс для обработки нажатий клавиш с защитой от дребезга (перелетов)."""

    last_state = {"up": False, "down": False, "left": False, "right": False,
                  "w": False, "s": False, "a": False, "d": False}
    
    confirm_keys = ["space", "enter"]

    @staticmethod
    def is_pressed(button: str) -> bool:
        """Проверяет, нажата ли клавиша прямо сейчас."""
        return keyboard.is_pressed(button)

    @staticmethod
    def get_vector_change() -> Vec2:
        """
        Возвращает вектор направления движения (WASD + стрелки),  
        но учитывает только изменения (нажатие впервые).
        """
        keys = {
            "left": keyboard.is_pressed("left") or keyboard.is_pressed("a"),
            "right": keyboard.is_pressed("right") or keyboard.is_pressed("d"),
            "up": keyboard.is_pressed("up") or keyboard.is_pressed("w"),
            "down": keyboard.is_pressed("down") or keyboard.is_pressed("s"),
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
        x = (keyboard.is_pressed("d") or keyboard.is_pressed("right")) - \
            (keyboard.is_pressed("a") or keyboard.is_pressed("left"))

        y = (keyboard.is_pressed("s") or keyboard.is_pressed("down")) - \
            (keyboard.is_pressed("w") or keyboard.is_pressed("up"))

        return Vec2(x, y)

    def is_confirmed() -> bool:
        return any(keyboard.is_pressed(key) for key in Controller.confirm_keys)
