from random import randint

import config
from objects.Hole import Hole
from objects.Player import Player


class Item:
    def __init__(self, radius: float, name: str):
        self.radius = radius
        self.x = randint(30, config.WIDTH - 40)
        self.y = randint(30, config.HEIGHT - 40)
        self.name = name

    def distance_to_object(self, obj) -> float:
        return ((self.x + self.radius // 2 - obj.x) ** 2 + (self.y + self.radius // 2 - obj.y) ** 2) ** 0.5

    def check_collision(self, hole: Hole, player: Player, items):
        while (self.distance_to_object(hole) < self.radius + config.ITEM_SPAWN_DISTANCE and
               self.distance_to_object(player) < self.radius + config.ITEM_SPAWN_DISTANCE and
               any(self.distance_to_object(item) < self.radius + config.ITEM_SPAWN_DISTANCE for item in items)):
            self.x = randint(30, config.WIDTH - 40)
            self.y = randint(30, config.HEIGHT - 40)
