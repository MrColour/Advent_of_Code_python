from collections import defaultdict

def get_square(x, y, spiral):
	total = 0
	total += spiral[(x - 1, y - 1)] + spiral[(x + 0, y - 1)] + spiral[(x + 1, y - 1)]
	total += spiral[(x - 1, y + 0)] + spiral[(x + 0, y + 0)] + spiral[(x + 1, y + 0)]
	total += spiral[(x - 1, y + 1)] + spiral[(x + 0, y + 1)] + spiral[(x + 1, y + 1)]
	# print(total)
	return (total)

input = open("input.txt").read()
input = int(input)

spiral = defaultdict(int)
spiral[(0, 0)] = 1
at = spiral[(0, 0)]

size = 2
dir_names = {0 : "UP", 1 : "LEFT", 2 : "DOWN", 3 : "RIGHT"}
direction = 0
coord = [1, -1]
while (at < input):
	for i in range(size):
		if (dir_names[direction] == "UP"):
			coord[1] += 1
		if (dir_names[direction] == "LEFT"):
			coord[0] -= 1
		if (dir_names[direction] == "DOWN"):
			coord[1] -= 1
		if (dir_names[direction] == "RIGHT"):
			coord[0] += 1

		at = get_square(coord[0], coord[1], spiral)
		spiral[(coord[0], coord[1])] = at

		if (at > input):
			print(at)
			exit()

	direction += 1
	direction %= 4
	if (direction == 0):
		coord[0] += 1
		coord[1] -= 1
		size += 2
