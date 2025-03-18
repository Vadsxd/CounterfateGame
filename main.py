import sys

import pygame

import config
from objects.Hole import Hole
from objects.Player import Player

# Инициализация pygame
pygame.init()

# Определение размеров окна
window = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Game with a Hole")

# Инициализация объектов
player = Player(config.PLAYER_SIZE, config.PLAYER_X, config.PLAYER_Y, config.PLAYER_SPEED)
hole = Hole(50, config.WIDTH // 2, config.HEIGHT // 2)

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

    # Проверка на падение в дыру
    distance_to_hole = ((player_x + player.size // 2 - hole.x) ** 2 +
                        (player_y + player.size // 2 - hole.y) ** 2) ** 0.5
    if distance_to_hole < hole.radius:
        print("Вы провалились в дыру!")
        running = False

    # Отрисовка
    window.fill(config.WHITE)  # Обновление фона
    pygame.draw.circle(window, config.RED, (hole.x, hole.y), hole.radius)
    pygame.draw.rect(window, config.BLACK, (player_x, player_y, player.size, player.size))

    pygame.display.flip()  # Обновление окна

    # Ограничение частоты кадров
    pygame.time.Clock().tick(config.FPS)

# Закрытие Pygame
pygame.quit()
sys.exit()
