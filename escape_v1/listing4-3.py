# Escape - A Python Adventure
# by Sean McManus/www.sean.co.uk
# Typed in by Matthew Eastman

import time
import random
import math


####################
#     VARIABLES    #
####################

WIDTH = 800  # Window Size
HEIGHT = 800

# PLAYER VARIABLES
PLAYER_NAME = "Matt"
FRIEND1_NAME = "Jordan"
FRIEND2_NAME = "Stephen"
current_room = 31  # start room = 31


top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]


###############
#     MAP     #
###############

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [["Room 0 - Where unused objects are kept", 0, 0, False, False]]

outdoor_rooms = range(1, 26)

for plantsectors in range(1, 26):  # rooms 1 - 25 are generated here
    GAME_MAP.append(["The dusty planet surface", 13, 13, True, True])

GAME_MAP += [
    ["The airlock", 13, 5, True, False],  # Room 26
    ["The engineering lab", 13, 13, False, False],  # Room 27
    ["Poodle Mission Control", 9, 13, False, True],  # Room 28
    ["The viewing gallery", 9, 15, False, False],  # Room 29
    ["The crew's bathroom", 5, 5, False, False],  # Room 30
    ["The airlock entry bay", 7, 11, True, True],  # Room 31
    ["Left elbow room", 9, 7, True, False],  # Room 32
    ["Right elbow room", 7, 13, True, True],  # Room 33
    ["The science lab", 13, 13, False, True],  # Room 34
    ["The greenhouse", 13, 13, True, False],  # Room 35
    [f"{PLAYER_NAME}" + "'s sleepig quarters", 9, 11, False, False],  # Room 36
    ["West corridor", 15, 5, True, True],  # Room 37
    ["The briefing room", 7, 13, False, True],  # Room 38
    ["The crew's community room", 11, 13, True, False],  # Room 39
    ["Main Mission Control", 14, 14, False, False],  # Room 40
    ["The sick bay", 12, 7, True, False],  # Room 41
    ["West corridor", 9, 7, True, False],  # Room 42
    ["Utilities control room", 9, 9, False, True],  # Room 43
    ["Systems engineering bay", 9, 11, False, False],  # Room 44
    ["Security portal to Mission Control", 7, 7, True, False],  # Room 45
    [f"{FRIEND1_NAME}" + "'s sleeping quarters", 9, 11, True, True],  # Room 46
    [f"{FRIEND2_NAME}" + "'s sleeping quarters", 9, 11, True, True],  # Room 47
    ["The pipeworks", 13, 11, True, False],  # Room 48
    ["The chief scientist's office", 9, 7, True, True],  # Room 49
    ["The robot workshop", 9, 11, True, False]  # Room 50
    ]

# dimple sanity check on map above to check data entry
assert len(GAME_MAP) - 1 == MAP_SIZE, "Map size and GAME_MAP dont match"

####################
#     MAKE MAP     #
####################

def get_floor_type():
    if current_room in outdoor_rooms:
        return 2  # soil
    else:
        return 0  # tiled floor


def generate_map():
    # This function makes the map for the current room,
    # using room data, scenery data and prop data.
    global room_map, room_width, room_height, room_name, hazard_map, \
        room_exit_top, room_exit_right
    global top_left_x, top_left_y, wall_transparency_frame

    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]
    room_exit_top = room_data[3]
    room_exit_right = room_data[4]

    floor_type = get_floor_type()
    if current_room in range(1, 21):
        bottom_edge = 2  # soil
        side_edge = 2  # soil
    if current_room in range(21, 26):
        bottom_edge = 1  # wall
        side_edge = 2  # soil
    if current_room > 25:
        bottom_edge = 1  # wall
        side_edge = 1  # wall

    # Create top line of room map.
    room_map = [[side_edge] * room_width]

    # Add middle lines of room map(wall, floor to fill width, wall).
    for y in range(room_height - 2):
        room_map.append([side_edge] + [floor_type] * (room_width - 2) +
                        [side_edge])

    # Add bottom line of room map
    room_map.append([bottom_edge] * room_width)

    # Add doorways
    middle_row = int(room_height / 2)
    middle_column = int(room_width / 2)

    if room_data[4]:  # If exit at right of this room
        room_map[middle_row][room_width - 1] = floor_type
        room_map[middle_row + 1][room_width - 1] = floor_type
        room_map[middle_row - 1][room_width - 1] = floor_type

    if current_room % MAP_WIDTH != 1:  # If room is not on lef of map
        room_to_left = GAME_MAP[current_room - 1]
        # If room on the left has an exit, add left exit in this room
        if room_to_left[4]:
            room_map[middle_row][0] = floor_type
            room_map[middle_row + 1][0] = floor_type
            room_map[middle_row - 1][0] = floor_type

    if room_data[3]:  # Exit at top of this room
        room_map[0][middle_column] = floor_type
        room_map[0][middle_column + 1] = floor_type
        room_map[0][middle_column - 1] = floor_type

    if current_room <= MAP_SIZE - MAP_WIDTH:  # If room is not bottom row
        room_below = GAME_MAP[current_room + MAP_WIDTH]
        # If room below has a top exit, add exit at bottom of this one
        if room_below[3]:
            room_map[room_height - 1][middle_column] = floor_type
            room_map[room_height - 1][middle_column + 1] = floor_type
            room_map[room_height - 1][middle_column - 1] = floor_type

####################
#     Explorer     #
####################

def draw():
    global room_height, room_width, room_map, room_name, room_exit_right, \
        room_exit_top

    generate_map()
    screen.clear()

    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw, (top_left_x + (x * 30),
                        top_left_y + (y * 30) - image_to_draw.get_height()))


def movement():
    global current_room
    old_room = current_room

    if keyboard.left:
        current_room -= 1
    if keyboard.right:
        current_room += 1
    if keyboard.up:
        current_room -= MAP_WIDTH
    if keyboard.down:
        current_room += MAP_WIDTH
    if keyboard.space:
        print(f"""The current room number is {current_room}
            Current room description: {room_name}
            The height of the room is {room_height}
            The width of the room is {room_width}
            There is an exit on the top?: {room_exit_top}
            There is an exit on the right?: {room_exit_right}
            """)

    if current_room > 50:
        current_room = 50
    if current_room <= 1:
        current_room = 1

    if current_room != old_room:
        print("Entering room:" + str(current_room))


clock.schedule_interval(movement, 0.1)
