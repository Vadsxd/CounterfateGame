import pygame
import sys

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

# Персонаж
player_size = 50
player_x = WIDTH // 2 - 200
player_y = HEIGHT // 2 - 200
player_speed = 5

# Дыра
hole_radius = 50
hole_x = WIDTH // 2
hole_y = HEIGHT // 2

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление персонажем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ограничение персонажа от выхода за границы экрана
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # Проверка на падение в дыру
    distance_to_hole = ((player_x + player_size // 2 - hole_x) ** 2 +
                        (player_y + player_size // 2 - hole_y) ** 2) ** 0.5
    if distance_to_hole < hole_radius:
        print("Вы провалились в дыру!")
        running = False

    # Отрисовка
    window.fill(WHITE)  # Обновление фона
    pygame.draw.rect(window, BLACK, (player_x, player_y, player_size, player_size))  # Отрисовка персонажа
    pygame.draw.circle(window, RED, (hole_x, hole_y), hole_radius)  # Отрисовка дыры

    pygame.display.flip()  # Обновление окна

    # Ограничение частоты кадров
    pygame.time.Clock().tick(30)

# Закрытие Pygame
pygame.quit()
sys.exit()
