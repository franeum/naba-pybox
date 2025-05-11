import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 150, 0)
CYAN = (0, 255, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

__colors = [RED, GREEN, BLUE, YELLOW, CYAN, PURPLE, WHITE]


def get_random_color():
    return random.choice(__colors)
