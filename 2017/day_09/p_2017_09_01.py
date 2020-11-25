def discard_garbage(input_string):
	in_garbage = False
	input_iter = iter(input_string)

	for c in input_iter:
		if (c == '!'):
			next(input_iter)
			continue
		if (c == '<'):
			in_garbage = True
		if (not in_garbage):
			yield c
		if (c == '>'):
			in_garbage = False

input = open("input.txt").read()

gen = discard_garbage(input)

score = 0
nest_level = 0
for c in gen:
	if (c == '{'):
		nest_level += 1
		score += nest_level
	if (c == '}'):
		nest_level -= 1

print(score)
