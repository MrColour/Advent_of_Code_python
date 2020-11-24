input = open("input.txt").read().rstrip()

input += input[0]

sum = 0
for i in range(len(input) - 1):
	if (input[i] == input[i + 1]):
		sum += int(input[i])

print(sum)