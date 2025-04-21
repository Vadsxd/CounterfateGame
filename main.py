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
hole = Hole(50, config.WIDTH // 2, config.HEIGHT // 2)
items = []

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление персонажем
    player.move()

    # Ограничение персонажа от выхода за границы экрана
    player_x = max(0, min(config.WIDTH - player.size, player.x))
    player_y = max(0, min(config.HEIGHT - player.size, player.y))

    # Спавн вещей
    # TODO: спавн не в дыре
    # TODO: скорость спавна вещей
    # TODO: спавн в дистанции от персонажа
    if len(items) < 10:
        item = Item(20, randint(30, config.WIDTH - 40), randint(30, config.HEIGHT - 40), "item")
        items.append(item)

    # Проверка на падение в дыру
    distance_to_hole = ((player_x + player.size // 2 - hole.x) ** 2 +
                        (player_y + player.size // 2 - hole.y) ** 2) ** 0.5
    if distance_to_hole < hole.radius:
        print("Вы провалились в дыру!")
        running = False

    # Проверка на подбор предмета
    for item in items:
        distance_to_item = ((player_x + player.size // 2 - item.x) ** 2 +
                            (player_y + player.size // 2 - item.y) ** 2) ** 0.5
        if distance_to_item < item.radius:
            print("Был подобран предмет", item.name)
            items.remove(item)

    # Отрисовка
    window.fill(config.WHITE)  # Обновление фона
    pygame.draw.circle(window, config.RED, (hole.x, hole.y), hole.radius)
    pygame.draw.rect(window, config.BLACK, (player_x, player_y, player.size, player.size))
    for item in items:
        pygame.draw.circle(window, config.GREEN, (item.x, item.y), item.radius)

    pygame.display.flip()  # Обновление окна

    # Ограничение частоты кадров
    pygame.time.Clock().tick(config.FPS)

# Закрытие Pygame
pygame.quit()
sys.exit()
