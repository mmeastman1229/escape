planets = {
    "Mercury": "The smallest planet, nearest the Sun"
    "Venus": "Venus takes 243 days to rotate"
    "Earth": "The only planet known to have native life"
    "Mars": "The Red Planet is the second smallest planet"
    "Jupiter": "The largest planet, Jupiter is a gas giant"
    "Saturn": "The second largest planet is a gas giant"
    "Uranus": "An ice giant with a ring system"
    "Neptune": "An ice giant farthest from the sun"
    "Pluto": "Largest dwarf planet in the Solary System"
}

while True:
    query = input("Which planet would you like information on?: ")
    if query in planets.keys():
        print(planets[query])
    else:
        print("No data available! Sorry!")
