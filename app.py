from time import sleep
from src.screen import Screen
from vec2 import Vec2
from src.scenes.menu import Menu


class Application:
    def __init__(self, w: int, h: int, fps: int, zoom_out: int):
        self.fps = fps
        self.zoom_out = zoom_out
        self.running = False
        self.screen = Screen(w, h)

        self.scenes = {"menu": Menu(self.screen.size)}
        self.active_scene = "menu"

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()
            sleep(1 / self.fps)
            
        self.exit()

    def update(self):
        result = self.scenes[self.active_scene].update()
        if not result:
            return
        match result:
            case "exit":
                exit()
            case _:
                self.active_scene = result

    def draw(self):
        self.screen.clear()

        self.scenes[self.active_scene].draw(self.screen)

        self.screen.refresh()