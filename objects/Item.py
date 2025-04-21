from random import randint

import config


class Item:
    def __init__(self, radius, name):
        self.radius = radius
        self.x = randint(30, config.WIDTH - 40)
        self.y = randint(30, config.HEIGHT - 40)
        self.name = name
