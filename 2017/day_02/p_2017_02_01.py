input = open("input.txt").read().rstrip()
# print(input)

rows = [list(map(int, row.split("\t"))) for row in input.split("\n")]
# print(rows)

total = [max(row) - min(row) for row in rows]
print(sum(total))


