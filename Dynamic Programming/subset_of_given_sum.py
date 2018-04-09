#Check subset exists

arr = [1,4,3,7,2,9,12,7,5]
summ = 12

def is_there_a_subset(arr, summ):
	n = len(arr)
	#Initialize the mem array
	mem = [[True]*(summ+1)]*(len(arr)+1)

	#If sum = 0, there exists an empty subset. Hence initialize to True
	for i in range(n+1):
		mem[i][0] = True

	#If array is empty and sum is not 0, there is no subset
	for i in range(1, summ+1):
		mem[0][i] = False

	for i in range(1, n+1):
		for j in range(1, summ+1):
			if j < arr[i-1]:
				mem[i][j] = mem[i-1][j]
			if j >= arr[i-1]:
				mem[i][j] = mem[i-1][j] or mem[i-1][j-arr[i-1]]
	return mem[n][summ]
print(is_there_a_subset(arr, summ))						