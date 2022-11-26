import pprint as pp


room_map = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

# print(room_map)

for y in range(6):
    print(room_map[y])

# Training missing 1
for i in range(3):
    print("Mayday!")
