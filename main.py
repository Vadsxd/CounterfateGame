from random import randint
import sys

import pygame

import config
from objects.Hole import Hole
from objects.Player import Player
from objects.Item import Item

# Инициализация pygame
pygame.init()

# Определение размеров окна
window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Game with a Hole")

# Инициализация объектов
player = Player(config.PLAYER_SIZE, config.PLAYER_X, config.PLAYER_Y, config.PLAYER_SPEED)
hole = Hole(config.HOLE_RADIUS, config.HOLE_X, config.HOLE_Y)
items = []
item_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(item_event_id, config.ITEM_SPAWN_RATE)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == item_event_id:
            if len(items) < config.ITEM_MAX:
                item = Item(config.ITEM_SIZE, "item")
                items.append(item)

    # Управление персонажем
    player.move()

    # Ограничение персонажа от выхода за границы экрана
    player_x = max(0, min(config.WIDTH - player.size, player.x))
    player_y = max(0, min(config.HEIGHT - player.size, player.y))

    # Спавн вещей
    # TODO: спавн не в дыре
    # TODO: спавн в дистанции от персонажа

    # Проверка на падение в дыру
    distance_to_hole = player.distance_to_object(hole)
    if distance_to_hole < hole.radius:
        print("Вы провалились в дыру!")
        running = False

    # Проверка на подбор предмета
    for item in items:
        distance_to_item = player.distance_to_object(item)
        if distance_to_item < item.radius:
            print("Был подобран предмет:", item.name)
            items.remove(item)

    # Отрисовка
    window.fill(config.WHITE)  # Обновление фона
    pygame.draw.circle(window, config.RED, (hole.x, hole.y), hole.radius)
    for item in items:
        pygame.draw.circle(window, config.GREEN, (item.x, item.y), item.radius)
    pygame.draw.rect(window, config.BLACK, (player_x, player_y, player.size, player.size))

    pygame.display.flip()  # Обновление окна

    # Ограничение частоты кадров
    pygame.time.Clock().tick(config.FPS)

# Закрытие Pygame
pygame.quit()
sys.exit()
