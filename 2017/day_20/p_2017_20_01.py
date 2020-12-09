import math

input = open("input.txt").read().splitlines()

def accel(a, b, c) -> int:
	return (math.sqrt(a ** 2 + b ** 2 + c ** 2))

particle = 0
lo = accel(11, 7, -9)
for indx, line in enumerate(input):
	a = (0, 0, 0)
	exp = line.replace("<", "(").replace(">", ")").replace("), ", ")\n")
	exec(exp)
	test = accel(*a)
	if (test < lo):
		lo = test
		at = indx

print(at)