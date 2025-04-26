from random import randint, choice, uniform
from typing import List

import config
from objects import Enemy, Hole, Player


class Item:
    def __init__(self):
        self.radius = config.ITEM_RADIUS
        self.x = randint(30, config.WIDTH - 40)
        self.y = randint(30, config.HEIGHT - 40)
        self.name = None
        self.heal_buff = None
        self.speed_buff = None
        self.damage_buff = None

    def create(self):
        self.name = choice(config.ITEM_NAMES)
        if self.name == "garbage":
            return
        elif self.name == "heal":
            self.heal_buff = 30
        elif self.name == "power":
            self.damage_buff = 10
        elif self.name == "speed":
            self.speed_buff = 1

    def distance_to_object(self, obj) -> float:
        return ((self.x + self.radius // 2 - obj.x) ** 2 + (self.y + self.radius // 2 - obj.y) ** 2) ** 0.5

    def check_collision(self, hole: Hole, player: Player, items, enemies: List[Enemy]):
        while True:
            self.x = uniform(30.0, config.WIDTH - config.ITEM_SPAWN_DISTANCE)
            self.y = uniform(30.0, config.HEIGHT - config.ITEM_SPAWN_DISTANCE)

            if (self.distance_to_object(hole) >= self.radius + config.ITEM_SPAWN_DISTANCE and
                    self.distance_to_object(player) >= self.radius + config.ITEM_SPAWN_DISTANCE and
                    all(self.distance_to_object(item) >= self.radius + config.ITEM_SPAWN_DISTANCE for item in
                        items) and
                    all(self.distance_to_object(enemy) >= self.radius + config.ITEM_SPAWN_DISTANCE for enemy in
                        enemies)):
                break
