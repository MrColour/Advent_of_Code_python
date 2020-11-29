from collections import defaultdict
input = open("input.txt").read().splitlines()

played = 0

alpha = [chr(c) for c in range(ord('a'), ord('z') + 1)]
reg = defaultdict(int)
for letter in alpha:
	reg[letter] = 0

i = 0
while (i < len(input)):
	comm = input[i].split()

	if ("snd" in comm):
		played = reg[comm[1]]
	elif ("rcv" in comm):
		if (reg[comm[1]] != 0):
			print(played)
			exit()
	else:
		if (comm[2].isdigit() or comm[2][0] == '-'):
			second = int(comm[2])
		else:
			second = reg[comm[2]]


	if ("set" in comm):
		reg[comm[1]] = second
	elif ("add" in comm):
		reg[comm[1]] += second
	elif ("mul" in comm):
		reg[comm[1]] *= second
	elif ("mod" in comm):
		reg[comm[1]] %= second
	elif ("jgz" in comm):
		jump = 0
		if (comm[1].isdigit() and int(comm[1]) > 0):
			i += second - 1
		elif (reg[comm[1]] > 0):
			i += second - 1

	i += 1

print(reg)