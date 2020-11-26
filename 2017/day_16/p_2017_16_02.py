from collections import defaultdict

input = open("input.txt").read().strip().split(",")

# print(input)

programs = [chr(c) for c in range(ord('a'), ord('p') + 1)]

# print(programs)
def dance(dance_set, programs):

	for ins in dance_set:
		if (ins[0] == 's'):
			amount = int(ins[1:])
			programs = programs[-amount:] + programs[:-amount]
		elif (ins[0] == 'x'):
			indx_a, indx_b = map(int, ins[1:].split("/"))
			programs[indx_a], programs[indx_b] = programs[indx_b], programs[indx_a]
		elif (ins[0] == 'p'):
			indx_a, indx_b = map(int, map(programs.index, ins[1:].split("/")))
			programs[indx_a], programs[indx_b] = programs[indx_b], programs[indx_a]

	return (programs)

visted = defaultdict(int)

cycle = 0
while (visted["".join(programs)] == 0):
	visted["".join(programs)] += 1
	programs = dance(input, programs)
	cycle += 1

times = 1000000000 % cycle

for _ in range(times):
	programs = dance(input, programs)

print("".join(programs))
