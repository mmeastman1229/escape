##############
## MAKE MAP ##
##############

def get_floor_type():
    if current_room in outdoor_rooms:
        return 2  # soil
    else:
        return 0  # tiled floor


def generate_map():
    # This function makes th emap for the current room,
    # using room data, scenery data and prop data.
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame

    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]

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

    # Add bottom lin of room map
    room_map.append([bottom_edge] * room_width)

    # Add doorways
    middle_row = int(room_height / 2)
    middle_column = int(room_width / 2)

    if room_data[4]:  # If exit at right of this room
        room_map[middle_row][room_width - 1] = floor_type
        room_map[middle_row + 1][room_width - 1] = floor_type
        room_map[middle_row - 1][room_width - 1] = floor_type

    if current_room % MAP_WIDTH != 1: #  If room is not on lef of map
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

