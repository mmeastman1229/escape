# Space Walk
# by Sean McManus
# www.sean.co.uk / www.nostarch.com

WIDTH = 800
HEIGHT = 600
player_x = 500
player_y = 550


def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.ship, (130, 150))
