def discard_garbage(input_string):
	in_garbage = False
	input_iter = iter(input_string)

	for c in input_iter:
		if (c == '!'):
			next(input_iter)
			continue
		if (c == '>'):
			in_garbage = False
		if (in_garbage):
			yield c
		if (c == '<'):
			in_garbage = True

input = open("input.txt").read()

gen = discard_garbage(input)

score = 0
for c in gen:
	score += 1

print(score)
