import ctypes
import time
from ctypes import wintypes
import sys
from vec2 import Vec2

# Подключение к Windows API
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Константы для событий ввода
INPUT_RECORD_MOUSE_EVENT = 0x0002
FROM_LEFT_1ST_BUTTON_PRESSED = 0x0001

# Структура COORD для представления координат курсора
class COORD(ctypes.Structure):
    _fields_ = [("X", wintypes.SHORT), ("Y", wintypes.SHORT)]

# Структура для хранения информации о событии мыши
class MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ("dwMousePosition", COORD),
        ("dwButtonState", wintypes.DWORD),
        ("dwControlKeyState", wintypes.DWORD),
        ("dwEventFlags", wintypes.DWORD),
    ]

# Структура события ввода
class INPUT_RECORD(ctypes.Structure):
    _fields_ = [("EventType", wintypes.WORD), ("Event", MOUSE_EVENT_RECORD)]

# Получаем дескриптор консоли
hStdIn = kernel32.GetStdHandle(-10)  # STD_INPUT_HANDLE

def get_mouse_state():
    """Возвращает координаты мыши и флаг нажатия кнопки."""
    # Буфер событий ввода
    buffer = (INPUT_RECORD * 1)()
    events_read = wintypes.DWORD()

    # Читаем события консоли
    if not kernel32.ReadConsoleInputW(hStdIn, buffer, 1, ctypes.byref(events_read)):
        return None  # Ошибка чтения

    # Проверяем, является ли событие событием мыши
    if buffer[0].EventType == INPUT_RECORD_MOUSE_EVENT:
        mouse_event = buffer[0].Event

        # Получаем координаты курсора
        mx, my = mouse_event.dwMousePosition.X // 2, mouse_event.dwMousePosition.Y  # Два символа = 1 ячейка

        # Проверяем, нажата ли левая кнопка мыши
        clicked = (mouse_event.dwButtonState & FROM_LEFT_1ST_BUTTON_PRESSED) != 0

        return (mx, my, clicked)

    return None  # Если событие не связано с мышью

class Screen:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        self.clear()

    def set_char(self, pos: Vec2, char: str) -> bool:
        if pos.x < 0 or pos.x > self.width or pos.y < 0 or pos.y > self.height:
            return False
        if len(char) > 1:
            raise TypeError("Can set only one character")
        self.buffer[round(pos.y)][round(pos.x * 2)] = ord(char)
        return True

    def set_pixel(self, pos: Vec2) -> bool:
        if pos.x < 0 or pos.x > self.width or pos.y < 0 or pos.y > self.height:
            return False
        char_now = chr(self.buffer[int(pos.y)][round(pos.x * 2)])
        new_char = "▀" if (pos.y - int(pos.y)) < 0.5 else "▄"
        if char_now == "█":
            return True
        elif not char_now in ["▀", "▄", "█"]:
            self.buffer[int(pos.y)][round(pos.x * 2)] = ord(new_char)
        elif char_now != new_char:
            self.buffer[int(pos.y)][round(pos.x * 2)] = ord("█")
        return True
    
    def draw_box(self, lt_pos: Vec2, rd_pos: Vec2, style: int = 0):
        # Проверка корректности координат
        x1, y1 = int(lt_pos.x), int(lt_pos.y)
        x2, y2 = int(rd_pos.x), int(rd_pos.y)
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Неверно заданы координаты углов: левый верхний должен быть меньше правого нижнего")
        
        # Определяем стили рамки
        styles = {
            0: {'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘', 'h': '─', 'v': '│'},
            1: {'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝', 'h': '═', 'v': '║'},
            2: {'tl': '+', 'tr': '+', 'bl': '+', 'br': '+', 'h': '-', 'v': '|'}
        }
        
        if style not in styles:
            raise ValueError("Недопустимый стиль рамки. Доступны: 0, 1, 2.")

        box_chars = styles[style]

        # Функция обработки наложения символов
        def merge_chars(existing, new):
            """Выбирает правильный символ пересечения при наложении рамок"""
            merge_map = {
    # Пересечение одиночных линий
    ('│', '─'): '┼', ('│', '═'): '╪', ('║', '─'): '╫', ('║', '═'): '╬',

    # Пересечение верхних углов с линиями
    ('┌', '─'): '┬', ('┌', '│'): '├', ('┐', '─'): '┬', ('┐', '│'): '┤',
    ('╔', '═'): '╦', ('╔', '║'): '╠', ('╗', '═'): '╦', ('╗', '║'): '╣',

    # Пересечение нижних углов с линиями
    ('└', '─'): '┴', ('└', '│'): '├', ('┘', '─'): '┴', ('┘', '│'): '┤',
    ('╚', '═'): '╩', ('╚', '║'): '╠', ('╝', '═'): '╩', ('╝', '║'): '╣',

    # Пересечение верхнего левого с нижним правым
    ('┌', '┘'): '┼', ('┘', '┌'): '┼',
    ('╔', '╝'): '╬', ('╝', '╔'): '╬',

    # Пересечение верхнего правого с нижним левым
    ('┐', '└'): '┼', ('└', '┐'): '┼',
    ('╗', '╚'): '╬', ('╚', '╗'): '╬',

    # Пересечение верхнего левого с нижним левым
    ('┌', '└'): '├', ('└', '┌'): '├',
    ('╔', '╚'): '╠', ('╚', '╔'): '╠',

    # Пересечение верхнего правого с нижним правым
    ('┐', '┘'): '┤', ('┘', '┐'): '┤',
    ('╗', '╝'): '╣', ('╝', '╗'): '╣',

    # Пересечение левого и правого одинарного с двойным
    ('│', '║'): '╫', ('║', '│'): '╫',

    # Пересечение верхнего левого одинарного с двойным
    ('┌', '╚'): '╠', ('╚', '┌'): '╠',
    ('┌', '╗'): '╦', ('╗', '┌'): '╦',

    # Пересечение верхнего правого одинарного с двойным
    ('┐', '╔'): '╦', ('╔', '┐'): '╦',
    ('┐', '╝'): '╣', ('╝', '┐'): '╣',

    # Пересечение нижнего левого одинарного с двойным
    ('└', '╔'): '╠', ('╔', '└'): '╠',
    ('└', '╝'): '╩', ('╝', '└'): '╩',

    # Пересечение нижнего правого одинарного с двойным
    ('┘', '╚'): '╩', ('╚', '┘'): '╩',
    ('┘', '╗'): '╣', ('╗', '┘'): '╣',
}
            if (existing, new) in merge_map:
                return merge_map[(existing, new)]
            if (new, existing) in merge_map:
                return merge_map[(new, existing)]
            return new

        x = x1 + 0.5
        old_char_top = chr(self.get_char(Vec2(x, y1)))
        old_char_bottom = chr(self.get_char(Vec2(x, y2)))
        self.set_char(Vec2(x, y1), merge_chars(old_char_top, box_chars['h']))
        self.set_char(Vec2(x, y2), merge_chars(old_char_bottom, box_chars['h']))
        for x in range(x1 + 1, x2):
            old_char_top = chr(self.get_char(Vec2(x, y1)))
            old_char_bottom = chr(self.get_char(Vec2(x, y2)))
            self.set_char(Vec2(x, y1), merge_chars(old_char_top, box_chars['h']))
            self.set_char(Vec2(x, y2), merge_chars(old_char_bottom, box_chars['h']))
            
            x += 0.5
            old_char_top = chr(self.get_char(Vec2(x, y1)))
            old_char_bottom = chr(self.get_char(Vec2(x, y2)))
            self.set_char(Vec2(x, y1), merge_chars(old_char_top, box_chars['h']))
            self.set_char(Vec2(x, y2), merge_chars(old_char_bottom, box_chars['h']))

        # Рисуем вертикальные линии
        for y in range(y1 + 1, y2):
            old_char_left = chr(self.get_char(Vec2(x1, y)))
            old_char_right = chr(self.get_char(Vec2(x2, y)))
            self.set_char(Vec2(x1, y), merge_chars(old_char_left, box_chars['v']))
            self.set_char(Vec2(x2, y), merge_chars(old_char_right, box_chars['v']))

        # Рисуем углы (с учетом возможных наложений)
        old_tl = chr(self.get_char(Vec2(x1, y1)))
        old_tr = chr(self.get_char(Vec2(x2, y1)))
        old_bl = chr(self.get_char(Vec2(x1, y2)))
        old_br = chr(self.get_char(Vec2(x2, y2)))

        self.set_char(Vec2(x1, y1), merge_chars(old_tl, box_chars['tl']))
        self.set_char(Vec2(x2, y1), merge_chars(old_tr, box_chars['tr']))
        self.set_char(Vec2(x1, y2), merge_chars(old_bl, box_chars['bl']))
        self.set_char(Vec2(x2, y2), merge_chars(old_br, box_chars['br']))

    def get_char(self, pos: Vec2):
        return self.buffer[int(pos.y)][round(pos.x * 2)]

    def refresh(self):
        print("\033[?25l", end="")
        print("\033[H", end="")
        text_buf = ""
        for line in self.buffer:
            for char in line:
                text_buf += chr(char)
            text_buf += "\n"
        text_buf = text_buf[:-1]
        print(text_buf, end="")

    def clear(self):
        self.buffer = [[ord(" ") for _ in range(self.width * 2)] for _ in range(self.height)]