input = open("input.txt").read().replace(":", "").splitlines()

firewall = []
for i, line in enumerate(input):
	depth, range = map(int, line.split())
	firewall.append((depth, range))

second = 0
while (1):
	found = False

	for scan in firewall:
		depth, range = scan
		if ((second + depth) % ((range * 2) - 2) == 0):
			found = True
			break

	if (found == False):
		break
	second += 1

print(second)