input = open("input.txt").read().rstrip()

N = len(input) // 2

sum = 0
for i in range(len(input) - 1):
	if (input[i] == input[(i + N) % len(input)]):
		sum += int(input[i])

print(sum)