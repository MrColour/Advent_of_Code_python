input = open("input.txt").read().replace(":", "").splitlines()

second = 0
severity = 0
for line in input:
	depth, range = map(int, line.split())
	if (depth % ((range * 2) - 2) == 0):
		severity += (depth * range)

print(severity)