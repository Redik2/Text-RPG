import random
import noise  # pip install noise

WORLD_SIZE = 256

class Tiles:
    PLAINS = 0
    HILLS = 1
    FOREST = 2
    MOUNTIANS = 3

class World:
    def __init__(self, seed=None):
        self.seed = seed or random.randint(0, 10000)
        random.seed(self.seed)
        self.world_map = self.generate_world()

    def generate_world(self):
        """Создает двумерный массив мира с биомами"""
        print("start generation")
        world = []
        scale = 100.0  # Чем больше, тем плавнее биомы
        for y in range(WORLD_SIZE):
            row = []
            for x in range(WORLD_SIZE):
                value = noise.snoise2(x / scale, y / scale, octaves=4, base=self.seed)
                #print(value)
                if value < -0.3:
                    row.append("~")  # Вода
                elif value < 0.3:
                    row.append(" ")  # Равнины
                elif value < 0.4:
                    row.append("^")  # Лес
                else:
                    row.append("#")  # Горы
            world.append(row)
        print("end generation")
        return world

    def print_world(self):
        for row in self.world_map:
            print("".join(row))

# Генерация мира и его вывод
world = World()
world.print_world()
