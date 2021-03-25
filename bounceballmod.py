from random import randint

size = [600, 600]

pink = (255, 255, 255)
BLACK = (0,0,0)

len_line = 80
num_lines = 7


def generate_coords(num, from_bottom):
	coords = []

	for i in range(num_lines):
		x1 = randint(0, 600 - len_line)
		x2 = x1+len_line

		if from_bottom:
			y1 = y2 = 600
		else:
			y1 = randint(0,600)
			y2 = y1

		coord = [[x1,y1], [x2,y2]]
		coords.append(coord)

	return coords