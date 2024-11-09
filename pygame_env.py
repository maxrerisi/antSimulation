import random
import pygame
from global_settings import SCREEN_WIDTH, SCREEN_HEIGHT, FOOD_RADIUS, ANT_RADIUS, HILL_POSITION


def display_screen(ants, food, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pygame Screen')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # draw anthill
        pygame.draw.circle(screen, (255, 255, 0), HILL_POSITION, 10)

        for coord in ants:
            pygame.draw.circle(screen, (255, 255, 255), coord,
                               ANT_RADIUS)
        for coord in food:
            pygame.draw.circle(screen, (255, 0, 0), coord,
                               FOOD_RADIUS)

        pygame.display.flip()

    pygame.quit()


# ants = [(random.randint(WIDTH_MIN, WIDTH_MAX), random.randint(
#     HEIGHT_MIN, HEIGHT_MAX)) for _ in range(100)]
# food = [(random.randint(WIDTH_MIN, WIDTH_MAX), random.randint(
#     HEIGHT_MIN, HEIGHT_MAX)) for _ in range(10)]
# print(ants)
# display_screen([(0, 0)], ants=ants, food=food)
