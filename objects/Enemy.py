from random import randint

import config


class Enemy:
    def __init__(self):
        self.size = None
        self.name = "name"
        self.x = randint(30, config.WIDTH - 40)
        self.y = randint(30, config.HEIGHT - 40)
        self.speed = None
        self.damage = None
        self.health = None

    def create(self):
        self.size = config.ENEMY_SIZE
        self.speed = config.ENEMY_SPEED
        self.damage = config.ENEMY_DAMAGE
        self.health = config.ENEMY_HEALTH
