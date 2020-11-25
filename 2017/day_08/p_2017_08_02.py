from collections import defaultdict
input = open("input.txt").read().splitlines()

regs = defaultdict(int)

hi = 0
for line in input:
	words = line.split()

	by = int(words[2])
	if (words[1] == "dec"):
		by *= -1

	exp = str(regs[words[4]]) + words[5] + words[6]

	# print(exp)
	if (eval(exp)):
		regs[words[0]] += by
		if (regs[words[0]] > hi):
			hi = regs[words[0]]

# print(regs)

print(hi)