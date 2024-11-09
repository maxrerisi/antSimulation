import random
import math
from global_settings import GLOBAL_HEIGHT, GLOBAL_WIDTH, NODE_RADIUS, NODE_COUNT, FOOD_PER_NODE

def node(x, y, count):
    out = []
    for _ in range(count):
        out.append((x + (math.cos(random.uniform(0,math.tau))*random.uniform(-NODE_RADIUS, NODE_RADIUS)), y + (math.sin(random.uniform(0,math.tau))*random.uniform(-NODE_RADIUS, NODE_RADIUS))))

    return out

def create_nodes():
    out = []
    for _ in range(NODE_COUNT):
        out.extend(node(random.uniform(0, GLOBAL_WIDTH), random.uniform(0, GLOBAL_HEIGHT), FOOD_PER_NODE))

    return out