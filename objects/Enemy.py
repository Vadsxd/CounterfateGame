from random import uniform
from typing import List

import config
from objects import Hole, Player, Item


class Enemy:
    def __init__(self):
        self.size = None
        self.name = "Enemy"
        self.x = uniform(30.0, config.WIDTH - config.ENEMY_SIZE)
        self.y = uniform(30.0, config.HEIGHT - config.ENEMY_SIZE)
        self.speed = None
        self.damage = None
        self.health = None

    def create(self):
        self.size = config.ENEMY_SIZE
        self.speed = config.ENEMY_SPEED
        self.damage = config.ENEMY_DAMAGE
        self.health = config.ENEMY_HEALTH

    def distance_to_object(self, obj) -> float:
        enemy_center_x = self.x + self.size / 2
        enemy_center_y = self.y + self.size / 2

        if hasattr(obj, "size"):
            obj_center_x = obj.x + obj.size / 2
            obj_center_y = obj.y + obj.size / 2
            return ((enemy_center_x - obj_center_x) ** 2 + (enemy_center_y - obj_center_y) ** 2) ** 0.5
        else:
            distance = ((enemy_center_x - obj.x) ** 2 + (enemy_center_y - obj.y) ** 2) ** 0.5
            return distance - obj.radius

    def check_collision(self, hole: Hole, player: Player, items: List[Item], enemies):
        while True:
            self.x = uniform(30.0, config.WIDTH - config.ENEMY_SPAWN_DISTANCE)
            self.y = uniform(30.0, config.HEIGHT - config.ENEMY_SPAWN_DISTANCE)

            if (self.distance_to_object(hole) >= self.size / 2 + config.ENEMY_SPAWN_DISTANCE and
                    self.distance_to_object(player) >= self.size / 2 + config.ENEMY_SPAWN_DISTANCE and
                    all(self.distance_to_object(item) >= self.size / 2 + config.ENEMY_SPAWN_DISTANCE for item in
                        items) and
                    all(self.distance_to_object(enemy) >= self.size / 2 + config.ENEMY_SPAWN_DISTANCE for enemy in
                        enemies)):
                break

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self) -> bool:
        return self.health <= 0
