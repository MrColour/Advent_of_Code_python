from collections import defaultdict
input = open("input.txt").read().split()

banks = list(map(int, input))

# print(input)

def redis(banks):
	loc = banks.index(max(banks))

	mem = banks[loc]
	banks[loc] = 0

	loc += 1
	while (mem != 0):
		loc %= len(banks)
		banks[loc] += 1
		loc += 1
		mem -= 1

	return (banks)


print(banks)
visited = defaultdict(int)
h_bank = tuple(banks)
visited[h_bank] = 1

cycles = 0
steps = 0
while (visited[h_bank] == 1):
	new = redis(banks)
	print(new)
	h_bank = tuple(new)
	visited[h_bank] += 1
	cycles += 1
	steps += 1

cycles = -1
loop = defaultdict(int)
while (loop[h_bank] <= 1):
	new = redis(banks)
	h_bank = tuple(new)
	loop[h_bank] += 1
	cycles += 1

print(cycles)