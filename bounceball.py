import pygame
from random import randint

pygame.init()

size = [600, 600]
screen = pygame.display.set_mode(size)

pink = (255, 255, 255)
BLACK = (0,0,0)

len_line = 80
num_lines = 5

coords = []
for i in range(num_lines):
	x1 = randint(0,500)
	x2 = x1+len_line

	y1 = randint(0,500)
	y2 = y1

	coord = [[x1,y1], [x2,y2]]
	coords.append(coord)


game_on = True
while game_on:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False

	screen.fill(pink)

	for coord in coords:
		pygame.draw.aalines(screen, BLACK, False, coord)
	
	pygame.display.flip()
