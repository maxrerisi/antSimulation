import time
from global_settings import ANT_SPEED, HILL_POSITION, GLOBAL_WIDTH, GLOBAL_HEIGHT, ANT_RADIUS, SQR_RADIUS_VISIBILITY, FOOD_RADIUS, FOOD_TO_REPRODUCE, TO_HOME_RANDOM_ANGLE, RANDOM_ANGLE
import random
import math
import pygame
from distance_calculation import square_distance
from food import Food
from phermone import Phermone
from food_node import create_nodes

pygame.init()
screen = pygame.display.set_mode((GLOBAL_WIDTH, GLOBAL_HEIGHT))
pygame.display.set_caption('Pygame Screen')


class Ant():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = ANT_SPEED if isinstance(ANT_SPEED, int) or isinstance(ANT_SPEED, float) else random.uniform(*ANT_SPEED)
        self.direction = random.uniform(0, 2*math.pi)
        self.has_food = False
        self.phermones = []

    def move(self):
        if self.has_food and square_distance(self.x, self.y, HILL_POSITION[0], HILL_POSITION[1]) < 10**2:
            self.has_food = False

        if self.has_food:
            self.direction_to_point(*HILL_POSITION)
            self.direction += random.uniform(-TO_HOME_RANDOM_ANGLE, TO_HOME_RANDOM_ANGLE)
            self.phermones.append(Phermone(self.x, self.y))

        else:
            self.direction += random.uniform(-RANDOM_ANGLE, RANDOM_ANGLE)

        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        if self.x > GLOBAL_WIDTH or self.x < 0 or self.y > GLOBAL_HEIGHT or self.y < 0:
            self.direction -= math.pi

    def direction_to_point(self, x, y):
        self.direction = math.atan2(y - self.y, x - self.x)

    def draw(self, screen):
        color = (0, 255, 0) if self.has_food else (255, 255, 255)
        self.draw_phermones(screen)
        pygame.draw.circle(screen, color, (self.x, self.y), ANT_RADIUS)

    def draw_phermones(self, screen):
        for ph in self.phermones:
            if ph.draw(screen):
                self.phermones.remove(ph)
    def check_phermones(self, phermones):
        if len(phermones) != 0:
            closest_phermones = sorted(phermones, key=lambda ph: square_distance(
                        self.x, self.y, *ph))[:5]
            furthest_from_hill = max(closest_phermones, key=lambda ph: square_distance(
                        *HILL_POSITION, *ph))
            if square_distance(self.x, self.y, *furthest_from_hill) <= SQR_RADIUS_VISIBILITY:
                self.direction_to_point(*furthest_from_hill)

    def check_food(self, food):
        if not self.has_food:
            for f in food:
                if square_distance(self.x, self.y, f[0], f[1]) < 9:
                    self.has_food = True
                    food.remove(f)
                    break
        if not self.has_food:
            closest_food = min(food, key=lambda f: square_distance(
                self.x, self.y, f[0], f[1]))
            
            if square_distance(self.x, self.y, *closest_food) < SQR_RADIUS_VISIBILITY:
                self.direction_to_point(*closest_food)


# ANTS = [Ant(random.randint(0, GLOBAL_WIDTH), random.randint(
#     0, GLOBAL_HEIGHT)) for _ in range(100)]
ANTS = [Ant(*HILL_POSITION) for _ in range(100)]

FOOD_COORDS = create_nodes()


# FOOD_COORDS = [(random.randint(0, GLOBAL_WIDTH), random.randint(
#     0, GLOBAL_HEIGHT)) for _ in range(1000)]
while True:
    removed = False
    for f in FOOD_COORDS:
        if square_distance(*HILL_POSITION, *f) < 75**2:
            FOOD_COORDS.remove(f)
            removed = True
            FOOD_COORDS.append((random.randint(0, GLOBAL_WIDTH), random.randint(
                0, GLOBAL_HEIGHT)))
    if not removed:
        break

iterations = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # draw anthill
    pygame.draw.circle(screen, (255, 255, 0), HILL_POSITION, 10)

    for food in FOOD_COORDS:
        Food(*food).draw(screen=screen)

    all_phermones = []
    for ant in ANTS:
        all_phermones.extend([(ph.x, ph.y) for ph in ant.phermones])
    for ant in ANTS:
        ant.draw(screen)
        ant.check_food(FOOD_COORDS)
        ant.check_phermones(all_phermones)
        cache = ant.has_food
        ant.move()
        if not ant.has_food and cache and FOOD_TO_REPRODUCE:
            ANTS.append(Ant(*HILL_POSITION))

    if iterations < 5:
        time.sleep(0.5)

    iterations += 1

    font = pygame.font.Font(None, 36)
    foodleft = len(FOOD_COORDS)
    antsleft = len(ANTS)
    text = f"Food remaining: {foodleft}\n Ants: {antsleft}"
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    # time.sleep(0.025)
    print(foodleft, antsleft)

pygame.quit()
