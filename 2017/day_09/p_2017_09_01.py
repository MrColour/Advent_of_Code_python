def discard_garbage(input_string):
	discarding, ignore_next = False, False
	for char in input_string:
		if ignore_next:
			ignore_next = False
			continue
		if char == '!':
			ignore_next = True
			continue
		if char == '<':
			discarding = True
		if not discarding:
			yield char
		if char == '>':
			discarding = False

input = open("test.txt").read()

gen = discard_garbage(input)

for i in gen:
	print(i)