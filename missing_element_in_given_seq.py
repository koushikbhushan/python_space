#code
"""
Given an array of size n-1 and given that there are numbers from 1 to n with one missing, the missing number is to be found.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.
The second line of each test case contains N-1 input C[i],numbers in array.

Output:

Print the missing number in array.

Constraints:

1 ≤ T ≤ 200
1 ≤ N ≤ 1000
1 ≤ C[i] ≤ 1000
"""
t = int(input())
for itert in range(0,t):
    size = int(input())
    a = list(map(int, input().split()))
    reqSum = ((size+1)*(size+2))/2
    actSum = sum(a)
    print(int(reqSum-actSum))