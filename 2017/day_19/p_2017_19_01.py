input = open("input.txt").read().splitlines()

dirs = {'D': (0, 1), 'U': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

x = input[0].index("|")
y = 0
prev = "|"
direction = 'D'
while prev != ' ':
	x += dirs[direction][0]
	y += dirs[direction][1]

	if (input[y][x] == '+'):
		if (direction in ("D", "U")):
			if (input[y][x + 1] == '-'):
				direction = "R"
			else:
				direction = "L"
		else:
			if (input[y + 1][x] == '|'):
				direction = "D"
			else:
				direction = "U"
	elif (input[y][x] not in ("|", "-")):
		print(input[y][x], end="")

	prev = input[y][x]

print()
