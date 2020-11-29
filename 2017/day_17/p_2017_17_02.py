input = open("input.txt").read()

zero = 0
front = 0
insert = 0
curr_pos = 0
step = int(input)
while (insert < 50000000):
	curr_pos += step
	curr_pos %= insert + 1
	if (curr_pos == zero):
		front = insert + 1
	curr_pos += 1
	insert += 1

print(front)