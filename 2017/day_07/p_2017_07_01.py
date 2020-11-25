from collections import defaultdict

input = open("input.txt").read().splitlines()

tree = defaultdict(list)

for line in input:
	words = line.split()
	tree[words[0]]

	if (len(words) > 3):
		tree[words[0]] = words[3:]

tagged = defaultdict(int)

for key in tree:
	tagged[key] += 1
	for child in tree[key]:
		if "," in child:
			child = child[:-1]
		tagged[child] += 1

ans = [key for key in tagged if tagged[key] == 1]

print(ans[0])
