import pygame


class Player:
    def __init__(self, size, x, y, speed):
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed

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

    def distance_to_object(self, obj):
        return ((self.x + self.size // 2 - obj.x) ** 2 + (self.y + self.size // 2 - obj.y) ** 2) ** 0.5
