# display settings
GLOBAL_WIDTH, GLOBAL_HEIGHT = 1000, 750

FOOD_RADIUS = 1.5
ANT_RADIUS = 2.5

HILL_POSITION = (GLOBAL_WIDTH//2, GLOBAL_HEIGHT//2)



# ant behavior settings
ANT_SPEED = (2.5,7.5) # either an int or a tuple. if tuple, make it length 2 for a range of speeds
# this is the squared radius of the visibility an ant has. for 100, it can see food within 10 units
SQR_RADIUS_VISIBILITY = 100
PHERMONE_STRENGTH = 100 # the number of frames the phermones will exist for
FOOD_TO_REPRODUCE = False # if True, the ants will duplicate when food is brought back to the hill.
TO_HOME_RANDOM_ANGLE = 1 # number of radians the ant can deviate from the direct path to the hill (works as a uniform distribution from - to +)
RANDOM_ANGLE = 0.3 # number of radians the ant can deviate from its current path assuming it doesn't have food (either random searching or going to food)
NODE_RADIUS = 25
NODE_COUNT, FOOD_PER_NODE = 5, 250


# calculated values that don't need to be changed
# HEIGHT_MIN, HEIGHT_MAX = -GLOBAL_HEIGHT // 2, GLOBAL_HEIGHT // 2
# WIDTH_MIN, WIDTH_MAX = -GLOBAL_WIDTH // 2, GLOBAL_WIDTH // 2
