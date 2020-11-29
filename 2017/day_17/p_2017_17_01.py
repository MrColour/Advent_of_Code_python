input = open("input.txt").read()

nums = [0]

insert = 1
curr_pos = 0
step = int(input)
while (insert <= 2017):
	curr_pos += step
	curr_pos %= len(nums)
	nums.insert(curr_pos + 1, insert)
	curr_pos += 1
	insert += 1

print(nums[nums.index(2017) + 1])