coords = {
		"n": (0, -1),
"nw": (-1, 0), "ne": (1, -1),
"sw": (-1, 1), "se": (1, 0),
		"s": (0, 1)
}

input = open("input.txt").read().strip().split(",")

axis_a = 0
axis_b = 0

for word in input:
	a, b = coords[word]

	axis_a += a
	axis_b += b

#Axis_a is a mixed axis.
print(axis_b - axis_a + axis_a)