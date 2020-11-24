input = open("input.txt").read().split()

ins = list(map(int, input))

ptr = 0
steps = 0
while (ptr < len(ins)):
	ins[ptr] += 1
	ptr += ins[ptr] - 1
	steps += 1

print(steps)
