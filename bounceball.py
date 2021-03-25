import pygame
from bounceballmod import *


pygame.init()
screen = pygame.display.set_mode(size)

coords = generate_coords(num_lines, False)
game_on = True

while game_on:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False

	screen.fill(pink)

	for coord in coords:
		#print(coord[0][1])
		coord[0][1] -= 0.1
		coord[1][1] -= 0.1

		if coord[0][1] < 0:
			coords.remove(coord)

			coords.append(generate_coords(1, True)[0])
			print(len(coords))

		pygame.draw.aalines(screen, BLACK, False, coord)
	
	pygame.display.flip()
