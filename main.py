import sys

import pygame

from Hole import Hole
from Player import Player

# Инициализация pygame
pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game with a Hole")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Инициализация объектов
player = Player(40, 200, 200, 5)
hole = Hole(50, WIDTH // 2, HEIGHT // 2)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление персонажем
    player.move()

    # Ограничение персонажа от выхода за границы экрана
    player_x = max(0, min(WIDTH - player.size, player.x))
    player_y = max(0, min(HEIGHT - player.size, player.y))

    # Проверка на падение в дыру
    distance_to_hole = ((player_x + player.size // 2 - hole.x) ** 2 +
                        (player_y + player.size // 2 - hole.y) ** 2) ** 0.5
    if distance_to_hole < hole.radius:
        print("Вы провалились в дыру!")
        running = False

    # Отрисовка
    window.fill(WHITE)  # Обновление фона
    pygame.draw.rect(window, BLACK, (player_x, player_y, player.size, player.size))  # Отрисовка персонажа
    pygame.draw.circle(window, RED, (hole.x, hole.y), hole.radius)  # Отрисовка дыры

    pygame.display.flip()  # Обновление окна

    # Ограничение частоты кадров
    pygame.time.Clock().tick(30)

# Закрытие Pygame
pygame.quit()
sys.exit()
