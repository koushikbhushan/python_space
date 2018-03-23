"""Replace every element with the greatest element on right side
Given an array of integers, replace every element with the next greatest element (greatest element on the right side) in the array. Since there is no element next to the last element, replace it with -1. For example, if the array is {16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.
"""

arr = [16, 17, 4, 3, 5, 2]

arr_length = len(arr)

i = arr_length - 1
max = -1
print(i)
while i >= 0:
	temp = arr[i]	
	arr[i] = max	
	if temp > max:
		max = temp
	i = i-1
	

print(arr)	