"""Find the two repeating elements in a given array
You are given an array of n+2 elements. All elements of the array are in range 1 to n. And all elements occur once except two numbers which occur twice. Find the two repeating numbers.

For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5

The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice. So the output should be 4 2."""
import math
arr = [4, 2, 4, 5, 2, 3, 1]

total = 0
prod = 1
for e in arr:
	total += e
	prod *= e
# a+b = total-n(n+1)/2
# a*b = prod/n!
# (a+b)2 - (a-b)2 = 4ab
# a-b = sqrt((a+b)2 - 4ab)


#a+b calculation
n = len(arr) - 2
to_be_total = total - (n * (n+1)//2)


#a*b calculation
fact = 1
for i in range(1,n+1):
	fact *= i
to_be_prod = prod // fact

sub = math.sqrt((to_be_total*to_be_total) - (4 * to_be_prod))

#Now we know a+b which is 'to_be_total' and a-b which is sub
# So a = (a+b + a-b) / 2
# b = (a+b - (a-b)) / 2
a = int(to_be_total + sub) // 2
b = int(to_be_total - sub) // 2

print(a,b)