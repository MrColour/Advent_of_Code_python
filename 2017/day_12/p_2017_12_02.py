from collections import defaultdict

graph = defaultdict(list)

input = open("input.txt").read().replace(',', '').splitlines()

# print(input)

for line in input:
	words = line.split()

	graph[words[0]] = words[2:]

tagged = defaultdict(int)

def graph_travel(name, children):
	if (tagged[name] >= 1):
		return

	tagged[name] += 1
	for child in children:
		graph_travel(child, graph[child])

# print(graph)

groups = 0
for key in graph:
	if (tagged[key] == 0):
		groups += 1
		graph_travel(key, graph[key])

print(groups)