import pygame

import config
from objects import Item


class Player:
    def __init__(self, size: float, x: int, y: int):
        self.size = size
        self.x = x
        self.y = y
        self.speed = config.PLAYER_START_SPEED
        self.damage = config.PLAYER_START_DAMAGE
        self.health = config.PLAYER_MAX_HEALTH
        self.max_health = config.PLAYER_MAX_HEALTH
        self.player_items = []

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def distance_to_object(self, obj) -> float:
        return ((self.x + self.size // 2 - obj.x) ** 2 + (self.y + self.size // 2 - obj.y) ** 2) ** 0.5

    def pick_up_item(self, item: Item):
        self.player_items.append(item)
        if item.name == "garbage":
            return
        elif item.name == "heal":
            self.health = min(self.max_health, self.health + item.heal_buff)
        elif item.name == "power":
            self.damage += item.damage_buff
        elif item.name == "speed":
            self.speed += item.speed_buff
