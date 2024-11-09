import random
import math
from global_settings import WIDTH, HEIGHT, NODE_RADIUS, NODE_COUNT, FOOD_PER_NODE

# TODO nodes not circular

def node(x, y, count):
    out = []
    for _ in range(count):
        out.append((x + (math.cos(random.uniform(0,math.tau))*random.uniform(-NODE_RADIUS, NODE_RADIUS)), y + (math.sin(random.uniform(0,math.tau))*random.uniform(-NODE_RADIUS, NODE_RADIUS))))

    return out

def create_nodes():
    out = []
    for _ in range(NODE_COUNT):
        x, y = random.uniform(0, WIDTH), random.uniform(0, HEIGHT)
        def is_valid_node(x, y):
            distance = math.sqrt((x - WIDTH//2) ** 2 + (y - HEIGHT//2) ** 2)
            return distance > (25 + NODE_RADIUS)


        while True:
            x, y = random.uniform(0, WIDTH), random.uniform(0, HEIGHT)
            if is_valid_node(x, y):
                break
        out.extend(node(x, y, FOOD_PER_NODE))

    return out