# https://www.acmicpc.net/problem/9095

import sys

t = int(sys.stdin.readline())
data = []
for _ in range(0, t):
    data.append(int(sys.stdin.readline()))
arr = [1, 2, 3]

def recursion_check(n, arr:list):
    
    if n <= 0:
        return

    for i in range(0, len(arr)):
        bridge = n-arr[i]
        
        if bridge > 0:
            recursion_check(bridge, arr)

        elif bridge == 0:
            global cnt
            cnt += 1
        elif bridge < 0:
            break

for i in range(0, len(data)):
    cnt = 0
    recursion_check(data[i], arr)
    print(cnt)