input = open("input.txt").read().rstrip()
# input = open("input_test.txt").read().rstrip()

total = 0

lines = input.split("\n")

def get_first_digit(line):
	for i in range(len(line)):
		if (line[i].isdigit()):
			return int(line[i])

# print(lines)


for idx in range(len(lines)):
	first_digit = get_first_digit(lines[idx]) * 10
	second_digit = get_first_digit(lines[idx][::-1])

	total += first_digit + second_digit

	# print(first_digit, second_digit)

print(total)