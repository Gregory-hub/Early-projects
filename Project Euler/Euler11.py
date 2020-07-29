file = open("file.txt", 'r')
data = [line.strip() for line in file]
file.close()

for k in range(len(data)):
	print(data[k])
print("\n")
nums = []
little_nums = []
for i in data:
	for n in range(len(i) - 1):
		if i[n] == 0 and i[n + 1] != " " or (i[n] != " " and i[n + 1] != " "):
			little_nums.append(int(i[n] + (i[n + 1])))
	nums.append(little_nums)
	little_nums = []
#for k in nums:
#	print(k)
#print("")


def max_horizontal_prod(nums):
	max_horizontal_prod = 0
	for i in range(len(nums)):
		for j in range(len(nums[i]) - 3):
			prod = nums[i][j] * nums[i][j + 1] * nums[i][j + 2] * nums[i][j + 3]
			if prod > max_horizontal_prod:
				max_horizontal_prod = prod
	return max_horizontal_prod


def max_vertical_prod(nums):
	max_vertical_prod = 0
	for i in range(len(nums) - 3):
		for j in range(len(nums[i])):
			prod = nums[i][j] * nums[i + 1][j] * nums[i + 2][j] * nums[i + 3][j]
			if prod > max_vertical_prod:
				max_vertical_prod = prod
	return max_vertical_prod


def max_left_to_right_diagonal_prod(nums):
	max_diagonal_prod = 0
	for i in range(len(nums) - 3):
		for j in range(len(nums[i]) - 3):
			prod = nums[i][j] * nums[i + 1][j + 1] * nums[i + 2][j + 2] * nums[i + 3][j + 3]
			if prod > max_diagonal_prod:
				max_diagonal_prod = prod
	return max_diagonal_prod


def max_right_to_left_diagonal_prod(nums):
	max_diagonal_prod = 0
	for i in range(len(nums) - 3):
		for j in range(3, len(nums[i])):
			prod = nums[i][j] * nums[i + 1][j - 1] * nums[i + 2][j - 2] * nums[i + 3][j - 3]
			if prod > max_diagonal_prod:
				max_diagonal_prod = prod
	return max_diagonal_prod


def max_diagonal_prod(nums):
	return max(max_right_to_left_diagonal_prod(nums), max_left_to_right_diagonal_prod(nums))


print(max_horizontal_prod(nums))
print(max_vertical_prod(nums))
print(max_diagonal_prod(nums), "\n")
print(max(max_horizontal_prod(nums), max_vertical_prod(nums), max_diagonal_prod(nums)))