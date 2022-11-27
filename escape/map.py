# Escape game map

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [["Room 0 - Where unused objects are kept", 0, 0, False, False]]

outdoor_rooms = range(1, 26)
for planetsectors in range(1, 26):  # rooms 1 - 25 are generated here
    GAME_MAP.append(["The dusty planet surface", 13, 13, True, True])

GAME_MAP += [
    # ["Room name", height, width, Top exit?, Right exit?]
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
    [f"{PLAYER_NAME}'s sleepig quarters", 9, 11, False, False],  # Room 36
    ["West corridor", 15, 5, True, True],  # Room 37
    ["The briefing room", 7, 13, False, True],  # Room 38
    ["The crew's community room", 11, 13, True, False],  # Room 39
    ["Main Mission Control", 14, 14, False, False],  # Room 40
    ["The sick bay", 12, 7, True, False],  # Room 41
    ["West corridor", 9, 7, True, False],  # Room 42
    ["Utilities control room", 9, 9, False, True],  # Room 43
    ["Systems engineering bay", 9, 11, False, False],  # Room 44
    ["Security portal to Mission Control", 7, 7, True, False],  # Room 45
    [f"{FRIEND1_NAME}'s sleeping quarters", 9, 11, True, True],  # Room 46
    [f"{FRIEND2_NAME}'s sleeping quarters", 9, 11, True, True],  # Room 47
    ["The pipeworks", 13, 11, True, False],  # Room 48
    ["The chief scientist's office", 9, 7, True, True],  # Room 49
    ["The robot workshop", 9, 11, True, False],  # Room 50
]
