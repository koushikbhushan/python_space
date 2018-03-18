#Can be acheived by moving individual elemnts or by using temp array
#In this code we are using juggling algorithm

def left_rotate(arr, d):
	n=len(arr)
	for i in range(gcd(d,n)):
		j=i
		temp = arr[i]
		while True:
			k=j+d
			if k >= n:
				k = k-n
			if k == i:
				break

			arr[j] = arr[k]
			j = k
		arr[j] = temp	

def gcd(d, n):
	if n == 0:
		return d	
	else:
		return gcd(n, d%n)

arr = [1,2,3,4,5,5,6]
left_rotate(arr, 2)	
print(arr)	