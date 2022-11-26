import random

# Application Settings
APP_WIDTH = 800
APP_HEIGHT = 800
TILE_SIZE = 30


PLAYER_NAME = "Matt"
FRIEND1_NAME = "Luke"
FRIEND2_NAME = "Noah"


LANDER_SECTOR = random.randint(1, 24)
LANDER_X = random.randint(2, 11)
LANDER_Y = random.randint(2, 11)


# Player Settings
PLAYER = {
    "left": [
        images.spacesuit_left,
        images.spacesuit_left_1,
        images.spacesuit_left_2,
        images.spacesuit_left_3,
        images.spacesuit_left_4,
    ],
    "right": [
        images.spacesuit_right,
        images.spacesuit_right_1,
        images.spacesuit_right_2,
        images.spacesuit_right_3,
        images.spacesuit_right_4,
    ],
    "up": [
        images.spacesuit_back,
        images.spacesuit_back_1,
        images.spacesuit_back_2,
        images.spacesuit_back_3,
        images.spacesuit_back_4,
    ],
    "down": [
        images.spacesuit_front,
        images.spacesuit_front_1,
        images.spacesuit_front_2,
        images.spacesuit_front_3,
        images.spacesuit_front_4,
    ],
}
PLAYER_SHADOW = {
    "left": [
        images.spacesuit_left_shadow,
        images.spacesuit_left_1_shadow,
        images.spacesuit_left_2_shadow,
        images.spacesuit_left_3_shadow,
        images.spacesuit_left_4_shadow,
    ],
    "right": [
        images.spacesuit_right_shadow,
        images.spacesuit_right_1_shadow,
        images.spacesuit_right_2_shadow,
        images.spacesuit_right_3_shadow,
        images.spacesuit_right_4_shadow,
    ],
    "up": [
        images.spacesuit_back_shadow,
        images.spacesuit_back_1_shadow,
        images.spacesuit_back_2_shadow,
        images.spacesuit_back_3_shadow,
        images.spacesuit_back_4_shadow,
    ],
    "down": [
        images.spacesuit_front_shadow,
        images.spacesuit_front_1_shadow,
        images.spacesuit_front_2_shadow,
        images.spacesuit_front_3_shadow,
        images.spacesuit_front_4_shadow,
    ],
}

PILLARS = [
    images.pillar,
    images.pillar_95,
    images.pillar_80,
    images.pillar_60,
    images.pillar_50,
]


# Colors
BLACK = (0, 0, 0)
BLUE = (0, 155, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (128, 0, 0)
WHITE_SMOKE = (245, 245, 245)
SPACE_STATION = (100, 100, 100)
GRAY_91 = (232, 232, 232)
DARK_GREY = (69, 69, 69)

# Room Maps
MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT
