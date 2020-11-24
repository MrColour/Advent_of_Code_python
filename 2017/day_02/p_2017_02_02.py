def divisible_nums(row):
	for i in range(len(row)):
		for j in range(i + 1, len(row)):
			if (row[i] % row[j] == 0 or row[j] % row[i] == 0):
				if (row[i] > row[j]):
					return (row[i] // row[j])
				else:
					return (row[j] // row[i])


input = open("input.txt").read().rstrip()

rows = [list(map(int, row.split("\t"))) for row in input.split("\n")]

total = [divisible_nums(row) for row in rows]

print(sum(total))