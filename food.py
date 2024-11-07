import pygame
from global_settings import FOOD_RADIUS


class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), FOOD_RADIUS)
