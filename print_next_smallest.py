"""
Given an array, print the next smallest elemnt in the array. If there is no immediate smallest element, print -1
"""
t = int(input())
for itert in range(0,t):
    size = int(input())
    a = list(map(int, input().split()))
    for i in range(1,size):
        if a[i] < a[i-1]:
            print(a[i], end=' ')
        else:
            print(-1, end=' ')
        i+=1
    print(-1) 