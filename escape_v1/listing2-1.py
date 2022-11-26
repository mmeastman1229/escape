import pprint as pp

room_map = [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 0, 0, 0, 4],
]

pp.pprint(room_map)
print(room_map[1][3])
print(room_map[3][1])
print(room_map[0][0])

room_map[0][0] = 5

pp.pprint(room_map)

room_map[4][4] = 6
print()
pp.pprint(room_map)
