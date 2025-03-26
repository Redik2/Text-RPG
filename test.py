import time

width, height = 20, 10  # Размер "экрана" в символах

def draw_frame(frame):
    buf = ""
    for y in range(height):
        for x in range(width):
            buf += frame[y][x]  # Выводим символ без перевода строки
        buf += "\n"  # Переход на новую строку
    print(buf)

frame1 = [["." for _ in range(width)] for _ in range(height)]
frame2 = [["#" for _ in range(width)] for _ in range(height)]

# Рисуем первый кадр
while 1:
    draw_frame(frame1)
    time.sleep(0.01)

    # Перемещаем курсор в начало экрана и рисуем второй кадр
    print("\033[H", end="")  # ANSI-код для возврата курсора в верхний левый угол
    draw_frame(frame2)
    time.sleep(0.01)
    print("\033[H", end="")  # ANSI-код для возврата курсора в верхний левый угол