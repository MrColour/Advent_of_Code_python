import math
from collections import defaultdict

input = open("input.txt").read().splitlines()

def accel(a, b, c) -> int:
	return (math.sqrt(a ** 2 + b ** 2 + c ** 2))

particles = []

for indx, line in enumerate(input):
	p = (0, 0, 0)
	v = (0, 0, 0)
	a = (0, 0, 0)
	exp = line.replace("<", "(").replace(">", ")").replace("), ", ")\n")
	exec(exp)

	particles.append((p, v, a))

	# print(exp)

# print(particles)


def update(particle):
	p = particle[0]
	v = particle[1]
	a = particle[2]

	v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
	p = (p[0] + v[0], p[1] + v[1], p[2] + v[2])

	particle = (p, v, a)

	return (particle)

LONG_TIME = 10000
# for i in range(LONG_TIME):
for i in range(LONG_TIME):

	parts = particles
	particles = []
	pos = defaultdict(list)

	for indx, particle in enumerate(parts):
		temp = update(particle)
		particles.append(temp)
		pos[temp[0]].append(indx)

	remove = []

	for item in pos.items():
		if (len(item[1]) > 1):
			for i, index in enumerate(item[1][::-1]):
				remove.append(particles[index])

	particles = list(set(particles) - set(remove))

print(len(particles))