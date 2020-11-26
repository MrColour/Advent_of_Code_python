lengths = list(map(int, open("input.txt").read().split(',')))
knot = list(range(255))

# print(knot)
# print(lengths)

skip_size = 0
current_pos = 0
start = len(knot) + 1
for length in lengths:

	# print(knot, "Pre")
	knot = knot[:length][::-1] + knot[length:]

	# print(knot, "Rot")

	current_pos = length + skip_size
	current_pos %= (len(knot))
	skip_size += 1
	start -= current_pos

	knot = knot[current_pos:] + knot[:current_pos]

start %= (len(knot))

print(knot[start], knot[start + 1], knot[start] * knot[start + 1])