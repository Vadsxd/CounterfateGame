from typing import List

import pygame

import config
from objects import Item, Enemy, Hole


class Player:
    def __init__(self):
        self.size = config.PLAYER_SIZE
        # (x,y) top left side of rect
        self.x = config.PLAYER_X
        self.y = config.PLAYER_Y
        self.name = "Player"
        self.speed = config.PLAYER_START_SPEED
        self.damage = config.PLAYER_START_DAMAGE
        self.attack_range = config.PLAYER_START_ATTACK_RANGE
        self.health = config.PLAYER_MAX_HEALTH
        self.max_health = config.PLAYER_MAX_HEALTH
        self.player_items = []

    def distance_to_object(self, obj) -> float:
        player_center_x = self.x + self.size / 2
        player_center_y = self.y + self.size / 2

        if hasattr(obj, "size"):
            obj_center_x = obj.x + obj.size / 2
            obj_center_y = obj.y + obj.size / 2
            return ((player_center_x - obj_center_x) ** 2 + (player_center_y - obj_center_y) ** 2) ** 0.5
        else:
            distance = ((player_center_x - obj.x) ** 2 + (player_center_y - obj.y) ** 2) ** 0.5
            return distance - obj.radius

    def is_attack_available(self, enemy: Enemy):
        return self.distance_to_object(enemy) <= self.attack_range + self.size / 2

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
