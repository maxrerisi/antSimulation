import time
from global_settings import ANT_SPEED, HILL_POSITION, SCREEN_WIDTH, SCREEN_HEIGHT, ANT_RADIUS, SQR_RADIUS_VISIBILITY, FOOD_RADIUS, FOOD_TO_REPRODUCE, TO_HOME_RANDOM_ANGLE, RANDOM_ANGLE, WIDTH, HEIGHT, SCALE_FACTOR, FONT_SIZE, FPS_UPDATE, ANT_COUNT, STUCK_THRESH, MOVE_CACHE, AMOUNT_OF_FOOD_TO_REPRODUCE, START_HEALTH
import random
import math
import pygame
from distance_calculation import square_distance
from food import Food
from phermone import Phermone
from food_node import create_nodes

pygame.init()
effective_grid = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Screen')
real_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Ant():
    def __init__(self, x, y, health = START_HEALTH):
        self.x = x
        self.y = y
        self.speed = ANT_SPEED if isinstance(ANT_SPEED, int) or isinstance(ANT_SPEED, float) else random.uniform(*ANT_SPEED)
        self.direction = random.uniform(0, 2*math.pi)
        self.has_food = False
        self.phermones = []
        self.recent_moves = [(0,0) for _ in range(MOVE_CACHE)]
        self.health = health

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
        if self.x > SCREEN_WIDTH or self.x < 0 or self.y > SCREEN_HEIGHT or self.y < 0:
            self.direction -= math.pi
        self.recent_moves.append((self.x, self.y))
        if square_distance(*self.recent_moves[0], *self.recent_moves[-1]) < STUCK_THRESH:
            self.direction_to_point(*HILL_POSITION)
        self.recent_moves.pop(0)
        self.health -= 0.1 if self.has_food else 1

    def direction_to_point(self, x, y):
        self.direction = math.atan2(y - self.y, x - self.x)

    def draw(self, screen):
        clr = min(255*self.health/START_HEALTH, 255)
        color = (0, 255, 0) if self.has_food else (clr,clr,clr)
        color = (255,0,255) if self.health > START_HEALTH else color
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
ANTS = [Ant(*HILL_POSITION) for _ in range(ANT_COUNT-1)]
ANTS.append(Ant(*HILL_POSITION, health=10*START_HEALTH))
FOOD_COORDS = create_nodes()


# FOOD_COORDS = [(random.randint(0, GLOBAL_WIDTH), random.randint(
#     0, GLOBAL_HEIGHT)) for _ in range(1000)]

hill_food = 0
last_delta_time = time.time()
iterations = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    effective_grid.fill((0, 0, 0))

    # draw anthill
    pygame.draw.circle(effective_grid, (255, 255, 0), HILL_POSITION, 10*SCALE_FACTOR*3//2)

    for food in FOOD_COORDS:
        Food(*food).draw(screen=effective_grid)

    max_life = 0
    all_phermones = []
    for ant in ANTS:
        all_phermones.extend([(ph.x, ph.y) for ph in ant.phermones])
    for ant in ANTS:
        ant.draw(effective_grid)
        ant.check_phermones(all_phermones)
        ant.check_food(FOOD_COORDS)
        cache = ant.has_food
        ant.move()
        if not ant.has_food and cache and FOOD_TO_REPRODUCE:
            hill_food += 1
            # ANTS.append(Ant(*HILL_POSITION))
        if ant.health > max_life:
            max_life = ant.health
        if ant.health <= 0:
            ANTS.remove(ant)
            continue
    max_life = round(max_life,2)
    for _ in range(hill_food//AMOUNT_OF_FOOD_TO_REPRODUCE):
        ANTS.append(Ant(*HILL_POSITION))
    
    hill_food -= (hill_food//AMOUNT_OF_FOOD_TO_REPRODUCE)*AMOUNT_OF_FOOD_TO_REPRODUCE

    # if iterations < 5:
    #     time.sleep(0.5)
    
    if iterations % FPS_UPDATE == 0:
        new_time = time.time()
        fps = ((new_time - last_delta_time)/FPS_UPDATE)**-1
        last_delta_time = new_time

    iterations += 1

    font = pygame.font.Font(None, FONT_SIZE)
    foodleft = len(FOOD_COORDS)
    antsleft = len(ANTS)
    if antsleft == 0:
        print("All ants dead")
        time.sleep(5)
        break
    text = f"Food: {foodleft}\n Ants: {antsleft}\n Hill Food: {hill_food}\n Frames: {iterations}\n FPS: {fps:.2f} \n Max Life: {max_life}"
    text = font.render(text, True, (255, 255, 255))
    effective_grid.blit(text, (10, 10))
    scaled_surface = pygame.transform.smoothscale(effective_grid, (SCREEN_WIDTH, SCREEN_HEIGHT))
    real_screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
    # time.sleep(0.025)
    print(foodleft, antsleft, hill_food, iterations, f"{fps:.2f}", max_life)

pygame.quit()
