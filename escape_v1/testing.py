testing.py
def testing_function_room_info():
    print(
        f"""
        X coordinate : {player_x}
        Y coordinate : {player_y}
        Current Room # : {current_room}
        Current Room Description: {room_name}
        Room Height: {room_height}
        Room Width: {room_width}
        Inventory : {in_my_pockets}
        Selected Inventory : {item_carrying}
        Player Frame : {player_frame}
        Player Direction : {player_direction}
    """
    )


    def draw():
        global room_height, room_width, room_map, room_name
        generate_map()
        screen.clear()

        for y in range(room_height):
            for x in range(room_width):
                if room_map[y][x] != 255:
                    image_to_draw = objects[room_map[y][x]][0]
                    screen.blit(
                        image_to_draw,
                        (
                            top_left_x + (x * TILE_SIZE),
                            top_left_y + (y * TILE_SIZE) - image_to_draw.get_height(),
                        ),
                    )
                if player_y == y:
                    image_to_draw = PLAYER[player_direction][player_frame]
                    screen.blit(
                        image_to_draw,
                        (
                            top_left_x
                            + (player_x * TILE_SIZE)
                            + (player_offset_x * TILE_SIZE),  # x
                            top_left_y
                            + (player_y * TILE_SIZE)  # y
                            + (player_offset_y * TILE_SIZE)
                            - image_to_draw.get_height()
                        )
                    )  # screen.blit(image, (x, y)) is how this function reads

#### Teleporter for testing
#### Remove this section for the real game
##    if keyboard.x:
##        current_room = int(input("Enter room number:"))
##        player_x = 2
##        player_y = 2
##        generate_map()
##        start_room()
##        sounds.teleport.play()
#### Teleport section ends
