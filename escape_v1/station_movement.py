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
        print(
            f"""The current room number is {current_room}
            Current room description: {room_name}
            The height of the room is {room_height}
            The width of the room is {room_width}
            There is an exit on the top?: {room_exit_top}
            There is an exit on the right?: {room_exit_right}
            """
        )

    if current_room > 50:
        current_room = 50
    if current_room <= 1:
        current_room = 1

    if current_room != old_room:
        print("Entering room:" + str(current_room))


clock.schedule_interval(movement, 0.1)
