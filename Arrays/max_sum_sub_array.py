arr = [-1,-2,4,3,-4, 5,-8, 4,6,7]

sum_so_far = 0
max_sum = 0
for e in arr:
	sum_so_far += e
	if sum_so_far < 0:
		sum_so_far = 0
	if sum_so_far > max_sum:
		max_sum = sum_so_far

print(max_sum)		