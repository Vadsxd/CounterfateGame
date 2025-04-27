import sys
import time

import pygame

import config
from objects.Enemy import Enemy
from objects.Hole import Hole
from objects.Item import Item
from objects.Player import Player

pygame.init()

# Определение размеров окна
window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Counterfate Game")

# Инициализация объектов
player = Player()
hole = Hole()

# Список вещей на экране
map_items = []

# Список противников на карте
map_enemies = []

# Таймер появления вещей и противников на экране (мс)
pygame.time.set_timer(config.ITEM_EVENT_ID, config.ITEM_SPAWN_RATE)
pygame.time.set_timer(config.ENEMY_EVENT_ID, config.ENEMY_SPAWN_RATE)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == config.ITEM_EVENT_ID:  # Спавн вещей
            if len(map_items) < config.ITEM_MAX:
                item = Item()
                item.create()
                item.check_collision(hole, player, map_items, map_enemies)
                map_items.append(item)
        elif event.type == config.ENEMY_EVENT_ID:
            if len(map_enemies) < config.ENEMY_MAX:  # Спавн противников
                enemy = Enemy()
                enemy.create()
                enemy.check_collision(hole, player, map_items, map_enemies)
                map_enemies.append(enemy)

    # Управление персонажем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x = max(player.x - player.speed, 0)
    if keys[pygame.K_RIGHT]:
        player.x = min(player.x + player.speed, config.WIDTH - player.size)
    if keys[pygame.K_UP]:
        player.y = max(player.y - player.speed, 0)
    if keys[pygame.K_DOWN]:
        player.y = min(player.y + player.speed, config.HEIGHT - player.size)

    # Проверка на падение в дыру
    distance_to_hole = player.distance_to_object(hole)
    if distance_to_hole < player.size / 2:
        print("Вы провалились в дыру!")
        running = False

    # Проверка на подбор предмета
    for item in map_items:
        distance_to_item = player.distance_to_object(item)
        if distance_to_item < player.size / 2:
            print("Был подобран предмет:", item.name)
            player.pick_up_item(item)
            map_items.remove(item)

    # Отрисовка
    window.fill(config.WHITE)  # Обновление фона
    pygame.draw.circle(window, config.RED, (hole.x, hole.y), hole.radius)

    # Отрисовка предметов
    for item in map_items:
        pygame.draw.circle(window, config.GREEN, (item.x, item.y), item.radius)

    # Отрисовка противников
    for enemy in map_enemies:
        pygame.draw.rect(window, config.PURPLE, (enemy.x, enemy.y, enemy.size, enemy.size))

    # Отрисовка игрока
    pygame.draw.rect(window, config.BLACK, (player.x, player.y, player.size, player.size))

    # Атака игрока
    if keys[pygame.K_SPACE]:
        current_time = time.time()
        if current_time - player.last_attack_time >= config.PLAYER_START_ATTACK_RATE:
            player.attack(map_enemies)
            player.last_attack_time = current_time
            pygame.draw.circle(window, config.BLACK,
                               (player.x + player.size / 2, player.y + player.size / 2), player.attack_range, width=1)

    # Обновление окна
    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.Clock().tick(config.FPS)

# Закрытие Pygame
pygame.quit()
sys.exit()
