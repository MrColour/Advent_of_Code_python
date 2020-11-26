input = open("input.txt").read()

seed_a, seed_b = [int(word) for word in input.split() if word.isdigit()]
factor_a, factor_b = 16807, 48271

def generator(seed, factor):
	num = seed

	while (1):
		num *= factor
		num %= 2147483647
		yield (num)

gen_a = generator(seed_a, factor_a)
gen_b = generator(seed_b, factor_b)

count = 0
for i in range(40000000):
	a = next(gen_a)
	b = next(gen_b)

	if (a & 0xffff == b & 0xffff):
		count += 1

print(count)