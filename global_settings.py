# display settings
GLOBAL_WIDTH, GLOBAL_HEIGHT = 1000, 750

FOOD_RADIUS = 1.5
ANT_RADIUS = 2.5

HILL_POSITION = (GLOBAL_WIDTH//2, GLOBAL_HEIGHT//2)


# ant behavior settings
ANT_SPEED = 1
# this is the squared radius of the visibility an ant has. for 100, it can see food within 10 units
SQR_RADIUS_VISIBILITY = 100


# calculated values that don't need to be changed
# HEIGHT_MIN, HEIGHT_MAX = -GLOBAL_HEIGHT // 2, GLOBAL_HEIGHT // 2
# WIDTH_MIN, WIDTH_MAX = -GLOBAL_WIDTH // 2, GLOBAL_WIDTH // 2
