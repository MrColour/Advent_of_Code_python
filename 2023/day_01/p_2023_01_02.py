input = open("input.txt").read().rstrip()
# input = open("input_test.txt").read().rstrip()

total = 0

lines = input.split("\n")

def calibration_num(string):
	storage = []

	key = 0
	value = 1

	matches = [
		["1", 1],
		["2", 2],
		["3", 3],
		["4", 4],
		["5", 5],
		["6", 6],
		["7", 7],
		["8", 8],
		["9", 9],
		["one", 1],
		["two", 2],
		["three", 3],
		["four", 4],
		["five", 5],
		["six", 6],
		["seven", 7],
		["eight", 8],
		["nine", 9],
	]

	for idx in range(len(matches)):
		if (string[0:len(matches[idx][key])] == matches[idx][key]):
			return matches[idx][value]


def get_first_digit(line):
	storage = []

	for i in range(len(line)):
		if (calibration_num(line[i:])):
			# print(calibration_num(line[i:]))
			storage.append(calibration_num(line[i:]))

	# print(storage)
	return (storage[0] * 10 + storage[-1])

# print(lines)

for idx in range(len(lines)):
	first_digit = get_first_digit(lines[idx])

	# print(first_digit)
	total += first_digit

print(total)