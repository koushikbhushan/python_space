from collections import deque
arr = [13, 11, 20, 4, 5, 7]


def nextGreaterElement(arr):
	queue = deque([])
	queue.append(arr[0])

	for i in range(1, len(arr)):
		element = queue.popleft()
		while element < arr[i]:
			print(str(element)+'->'+str(arr[i]))
			
			if len(queue) == 0:
				break
			element = queue.popleft()	
		if element > arr[i]:
			queue.append(element)

		queue.append(arr[i])
		
	while(len(queue) > 0):
		element = queue.popleft()
		next_el = '-1'
		print(str(element)+'->'+next_el)

nextGreaterElement(arr)					