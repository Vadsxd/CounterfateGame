from random import uniform, randint
from typing import List

import config
from objects import Hole, Player, Item


class Enemy:
    def __init__(self):
        self.size = None
        self.name = "Enemy"
        self.x = randint(30, config.WIDTH - config.ENEMY_SIZE)
        self.y = randint(30, config.HEIGHT - config.ENEMY_SIZE)
        self.speed = None
        self.damage = None
        self.health = None

    def create(self):
        self.size = config.ENEMY_SIZE
        self.speed = config.ENEMY_SPEED
        self.damage = config.ENEMY_DAMAGE
        self.health = config.ENEMY_HEALTH

    def distance_to_object(self, obj) -> float:
        return ((self.x + self.size // 2 - obj.x) ** 2 + (self.y + self.size // 2 - obj.y) ** 2) ** 0.5

    def check_collision(self, hole: Hole, player: Player, items: List[Item], enemies):
        while True:
            self.x = uniform(30.0, config.WIDTH - config.ENEMY_SPAWN_DISTANCE)
            self.y = uniform(30.0, config.HEIGHT - config.ENEMY_SPAWN_DISTANCE)

            if (self.distance_to_object(hole) >= self.size + config.ENEMY_SPAWN_DISTANCE and
                    self.distance_to_object(player) >= self.size + config.ENEMY_SPAWN_DISTANCE and
                    all(self.distance_to_object(item) >= self.size + config.ENEMY_SPAWN_DISTANCE for item in
                        items) and
                    all(self.distance_to_object(enemy) >= self.size + config.ENEMY_SPAWN_DISTANCE for enemy in
                        enemies)):
                break
