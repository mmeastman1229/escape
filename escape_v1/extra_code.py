use_message = """>> MESSAGE: "You fiddle around with it but don\'t get anywhere" """
standard_responses = {
    4: f""">> MESSAGE: "Air is running out! You can\'t take this lying down!" """,
    6: f""">> MESSAGE: "This is not time to sit around!" """,
    7: f""">> MESSAGE: "This is not time to sit around!" """,
    32: f""">> MESSAGE: "It shakes and rumbles, but nothing else happens" """,
    34: f""">> MESSAGE: "Ah! That's better. Now wash your hands" """,
    35: f""">> MESSAGE: "You wash your hands and shake the water off" """,
    37: f""">> MESSAGE: "The test tubes smoke slightly as you shake them" """,
    54: f""">> MESSAGE: "You chew the gum. It's sticky like glue" """,
    55: f""">> MESSAGE: "The yoyo bounces up and down, slightly slower than on earth" """,
    56: f""">> MESSAGE: "It's a bit too fiddly. Can you thread it on something" """,
    59: f""">> MESSAGE: "You need to fix the leak before you can use the canister" """,
    61: f""">> MESSAGE: "You try signalling with the mirror, but nobody can see you" """,
    62: f""">> MESSAGE: "Don't throw resources away. Things may come in handy..." """,
    67: f""">> MESSAGE: "To enjoy yummy space food, just add water!" """,
    75: f""">> MESSAGE: "You are in Sector: {current_room}
    ... //X: {player_x}  //Y: {player_y})"""



    screen.draw.text("Text color", (50, 30), color="orange")
    screen.draw.text("Font name and size", (20, 100), fontname="Boogaloo", fontsize=60)
    screen.draw.text("Positioned text", topright=(840, 20))
    screen.draw.text("Allow me to demonstrate wrapped text.", (90, 210), width=180, lineheight=1.5)
    screen.draw.text("Outlined text", (400, 70), owidth=1.5, ocolor=(255,255,0), color=(0,0,0))
    screen.draw.text("Drop shadow", (640, 110), shadow=(2,2), scolor="#202020")
    screen.draw.text("Color gradient", (540, 170), color="red", gcolor="purple")
    screen.draw.text("Transparency", (700, 240), alpha=0.1)
    screen.draw.text("Vertical text", midleft=(40, 440), angle=90)
    screen.draw.text("All together now:\nCombining the above options",
        midbottom=(427,460), width=360, fontname="Boogaloo", fontsize=48,
        color="#AAFF00", gcolor="#66AA00", owidth=1.5, ocolor="black", alpha=0.8)
