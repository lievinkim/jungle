# https://www.acmicpc.net/problem/1920

import sys
t = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

# for i in range(1, t):
#     for j in range(0, i):
#         if data[i] < data[j]:
#             data[i], data[j] = data[j], data[i]
data.sort()

def binary_search(arr:list, value:int):
    pl = 0
    pr = len(arr)-1

    while pl <= pr:
        pc = (pl+pr)//2
        if value < arr[pc]:
            pr = pc-1
        elif value > arr[pc]:
            pl = pc+1
        elif value == arr[pc]:
            print(1)
            return
    
    print(0)

d = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
for x in lst:
    binary_search(data, x)