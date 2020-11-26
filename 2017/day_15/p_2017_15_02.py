input = open("input.txt").read()

seed_a, seed_b = [int(word) for word in input.split() if word.isdigit()]
factor_a, factor_b = 16807, 48271

def generator(seed, factor, multi=1):
	num = seed

	while (True):
		num *= factor
		num %= 2147483647
		if (num % multi == 0):
			yield (num)

gen_a = generator(seed_a, factor_a, 4)
gen_b = generator(seed_b, factor_b, 8)

count = 0
for i in range(5000000):
	a = next(gen_a)
	b = next(gen_b)
	if (a & 0xffff == b & 0xffff):
		count += 1

print(count)