# display settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 750 # display size
SCALE_FACTOR = 2 # the factor by which the display is scaled up
WIDTH, HEIGHT = SCREEN_WIDTH*SCALE_FACTOR, SCREEN_HEIGHT*SCALE_FACTOR # the actual size of the display
FOOD_RADIUS = 1.5*SCALE_FACTOR
ANT_RADIUS = 2.5*(SCALE_FACTOR**2)

HILL_POSITION = (SCREEN_WIDTH*SCALE_FACTOR//2, SCREEN_HEIGHT*SCALE_FACTOR//2)



# ant behavior settings
ANT_SPEED = (2.5,7.5) # either an int or a tuple. if tuple, make it length 2 for a range of speeds
# this is the squared radius of the visibility an ant has. for 100, it can see food within 10 units
SQR_RADIUS_VISIBILITY = 100
PHERMONE_STRENGTH = 500 # the number of frames the phermones will exist for
FOOD_TO_REPRODUCE = True # if True, the ants will duplicate when food is brought back to the hill.
AMOUNT_OF_FOOD_TO_REPRODUCE = 10 # the number of food the ant needs to bring back to the hill to reproduce
TO_HOME_RANDOM_ANGLE = 1 # number of radians the ant can deviate from the direct path to the hill (works as a uniform distribution from - to +)
RANDOM_ANGLE = 0.3 # number of radians the ant can deviate from its current path assuming it doesn't have food (either random searching or going to food)
NODE_RADIUS = 25*SCALE_FACTOR # changes the distribution of food within a node
NODE_COUNT, FOOD_PER_NODE = 10, 500 
FPS_UPDATE = 3 # the number of frames for the FPS to update
ANT_COUNT = 10 # the number of ants to start with
STUCK_THRESH = 16 # the squared value of net displacement over MOVE_CACHE to warrant a shift in direction towards the hill
MOVE_CACHE = 10

# calculated values that don't need to be changed
# HEIGHT_MIN, HEIGHT_MAX = -GLOBAL_HEIGHT // 2, GLOBAL_HEIGHT // 2
# WIDTH_MIN, WIDTH_MAX = -GLOBAL_WIDTH // 2, GLOBAL_WIDTH // 2

FONT_SIZE = 36*SCALE_FACTOR