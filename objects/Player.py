from typing import List

import pygame

import config
from objects import Item, Enemy


class Player:
    def __init__(self):
        self.size = config.PLAYER_SIZE
        self.x = config.PLAYER_X
        self.y = config.PLAYER_Y
        self.name = "Player"
        self.speed = config.PLAYER_START_SPEED
        self.damage = config.PLAYER_START_DAMAGE
        self.attack_range = config.PLAYER_START_ATTACK_RANGE
        self.health = config.PLAYER_MAX_HEALTH
        self.max_health = config.PLAYER_MAX_HEALTH
        self.player_items = []

    def action(self, enemies: List[Enemy]):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_SPACE]:
            self.attack(enemies)

    def distance_to_object(self, obj) -> float:
        return ((self.x + self.size // 2 - obj.x) ** 2 + (self.y + self.size // 2 - obj.y) ** 2) ** 0.5

    def is_attack_available(self, enemy: Enemy):
        return self.distance_to_object(enemy) < self.attack_range

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

    def attack(self, enemies: List[Enemy]):
        for enemy in enemies:
            if self.is_attack_available(enemy):
                enemy.take_damage(self.damage)
                if enemy.is_dead():
                    enemies.remove(enemy)
