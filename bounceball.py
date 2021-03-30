import pygame
from bounceballmod import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)

    coords = generate_coords(num_lines, False)
    game_on = True

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        draw_paddles(coords, screen, speed)


if __name__ == "__main__":
    main()
