input = open("input.txt").read()

input = int(input)

# print(input)

i = 1
corner = 0
while (corner < input):
	corner = i * i
	i += 2

size = i - 2 - 1
while ((corner - size <= input <= corner) == False):
	corner -= size

i -= 2
dif = corner - input
print(i // 2 + abs(dif - size // 2))
