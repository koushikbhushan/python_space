arr = [2,1,3,1,2,2,1]
#Method 1
print('Method1 with n^2 complexity')
for i in range(len(arr)):
	if(sum(arr[:i+1]) == sum(arr[i+1:])):
		print(i)

print('Method2 with n^2 complexity')
for i in range(len(arr)):
	left_sum = 0
	right_sum = 0
	for j in range(i+1):
		left_sum += arr[j]

	for j in range(i+1,len(arr)):
		right_sum += arr[j]

	if(left_sum == right_sum):
		print(i)


#Method 3 with O(n) complexity
print('Method3 with O(n) complexity')
total = 0
for i in range(len(arr)):
	total += arr[i]
left_sum = 0
right_sum = 0	
for i in range(len(arr)):
	left_sum += arr[i]
	right_sum = total - left_sum
	if(left_sum == right_sum):
		print(i)
