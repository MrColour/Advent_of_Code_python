from collections import defaultdict

input = open("input.txt").read().splitlines()

tree = defaultdict(list)
weights = {}

for line in input:
	words = line.split()
	tree[words[0]]

	weights[words[0]] = int(words[1][1:-1])

	if (len(words) > 3):
		tree[words[0]] = words[3:]

print(tree)
# print(weights)
# print(tree["ddneaes"])

# print(weights["utnrb"])

def out(name, node):
	print(name)
	print("Run the program again.")
	print("Print the weight before calculation of node that is not balanced.")
	for child in node:
		if ("," in child):
			child = child[:-1]

		print(child, weights[child])


def recurse(name, node) -> int:
	# print(name)
	for child in node:
		if ("," in child):
			child = child[:-1]
		weights[child] = recurse(child, tree[child]) + weights[child]

	if (len(node) == 0):
		return (0)

	match = weights[node[0][:-1] if "," in node[0] else node[0]]
	for child in node:
		if ("," in child):
			child = child[:-1]
		if (weights[child] != match):
			out(name, node)
			exit()
	return (match * len(node))


recurse("bsfpjtc", tree["bsfpjtc"])