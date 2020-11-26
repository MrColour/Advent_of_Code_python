input = open("input.txt").read().strip().split(",")

# print(input)

programs = [chr(c) for c in range(ord('a'), ord('p') + 1)]

# print(programs)

for ins in input:
	if (ins[0] == 's'):
		amount = int(ins[1:])
		programs = programs[-amount:] + programs[:-amount]
	elif (ins[0] == 'x'):
		indx_a, indx_b = map(int, ins[1:].split("/"))
		programs[indx_a], programs[indx_b] = programs[indx_b], programs[indx_a]
	elif (ins[0] == 'p'):
		indx_a, indx_b = map(int, map(programs.index, ins[1:].split("/")))
		programs[indx_a], programs[indx_b] = programs[indx_b], programs[indx_a]

print("".join(programs))