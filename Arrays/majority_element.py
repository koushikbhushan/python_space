#Find majority element in an array
#A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element)

#1. Using HashMap/Dict

arr = [2,1,5,1,8,9,1,4,1,1,1,1,1,1]
val_count = {}

for element in arr:
	if element in val_count:
		val_count[element]+=1
	else:
		val_count[element] = 1
major = next(iter(val_count))
		
for key,val in val_count.items():
	if val > val_count[major]:
		major = key
if val_count[major]>=len(arr)/2:		
	print('Major element is: ',major)
else:
	print('No major element')	

#######################################################################
#2. Using Moore’s Voting Algorithm
def find_candidate(arr):
	maj_index, count = 0,1
	for i in range(len(arr)):
		if arr[maj_index] == arr[i]:
			count+=1
		else:
			count -=1

		if count == 0:
			maj_index = i
			count = 1
	return arr[maj_index]			

maj_candidate=find_candidate(arr)
count = 0
for element in arr:
	if element == maj_candidate:
		count+=1
if count >= len(arr)/2:
	print('Maj element using Moore\'s voting is', maj_candidate)
else:
	print('No major element found(Using Moore\'s voting)')		