from random import randint
import pygame


screen_height = 600
screen_width = 600
len_line = 80
num_lines = 7
speed = 0.1
start = 0
size = [screen_width, screen_height]

# colors
GREEN = (102, 255, 102)
BLACK = (0, 0, 0)


def generate_coords(num, from_bottom):
    """
    coordinates will be generated as below

    coords = [
                [[x1,y1],[x2,y2]],
                [[x1,y1],[x2,y2]],
                ...
            ]

    the num of coordinate in the coordinates (plural) list
    would be equal to the arg num

    if from_bottom is True, then the coordinates y1 and y2
    would be equal to the screen bottom points ie., screen height

    returns coordinates (plural)
    """
    coords = []

    for _ in range(num):
        x1 = randint(start, screen_width - len_line)
        x2 = x1+len_line

        if from_bottom:
            y1 = y2 = screen_height
        else:
            y1 = y2 = randint(start, screen_height)

        coord = [[x1, y1], [x2, y2]]
        coords.append(coord)

    return coords


def draw_paddles(coords, screen, speed):
    """
    draws paddles in the given screen
    moves the paddles in the give speed

    paddles are drawn in the given coordinate positions
    """
    screen.fill(BLACK)

    for coord in coords:
        coord[0][1] -= speed
        coord[1][1] -= speed

        if coord[0][1] < start:
            coords.remove(coord)
            coords.append(generate_coords(1, True)[0])

        pygame.draw.aalines(screen, GREEN, False, coord)
    pygame.display.flip()
