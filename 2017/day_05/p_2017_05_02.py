input = open("input.txt").read().split()

ins = list(map(int, input))

ptr = 0
steps = 0
while (ptr < len(ins)):
	temp = ins[ptr]
	ins[ptr] += -1 if ins[ptr] >= 3 else 1
	ptr += temp
	steps += 1

print(steps)
