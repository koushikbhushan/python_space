"""
Find subset of elements that are selected from a given set whose sum adds up to a given number K
"""
def find_subset(arr, subset, given_sum, curr_sum, i):
	if(given_sum == curr_sum):
		print('Sum ',curr_sum)
		print(subset)
	elif(i >= len(arr)):
		return
		
	else:
		#Add current element and try
		subset.append(arr[i])
		find_subset(arr, subset, given_sum, curr_sum+arr[i], i+1)

		#Try without adding current element
		subset.remove(arr[i])
		find_subset(arr, subset, given_sum, curr_sum, i+1)




def read_input():
	arr = list(map(int, input('Enter the list of elements').split()))
	given_sum = int(input('Enter the target sum'))
	return arr,given_sum

if __name__ == '__main__':
	arr,given_sum = read_input()
	subset = []
	curr_sum = 0
	find_subset(arr, subset, given_sum, curr_sum, 0)

