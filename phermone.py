import pygame
from global_settings import PHERMONE_STRENGTH, ANT_RADIUS

class Phermone():
    def __init__(self, x, y):
        self.strength = PHERMONE_STRENGTH
        self.x = x
        self.y = y

    def draw(self, screen):
        # print the x and y coordinates:
        self.strength -= 1
        pygame.draw.circle(screen, (0,0,255*self.strength/PHERMONE_STRENGTH), (self.x, self.y), ANT_RADIUS*0.75)
        return self.strength <= 0