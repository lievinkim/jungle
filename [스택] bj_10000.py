# https://www.acmicpc.net/problem/10000

import sys
t = int(sys.stdin.readline())
data = []
for _ in range(0, t):
    a, b = map(int, sys.stdin.readline().split())
    data.append([a-b, a+b])
data.sort(key=lambda x: (x[0],-x[1]))

linked = []
cnt = 0

def merge_arr(arr):
    global cnt
    global linked

    if len(arr) == 1:
        return arr

    end = arr[0][1]
    point = 1

    for i in range(1, len(arr)):
        if arr[i][0] >= end:
            point = i
            break
    
    left_arr = merge_arr(arr[:point])
    right_arr = merge_arr(arr[point:])
    
    if left_arr[0][1] == right_arr[0][0]:
        linked.append([left_arr[0][0], right_arr[0][1]])

    next_item = [[left_arr[0][0], right_arr[0][1]]]

    return next_item

merge_arr(data)

for item in data:
    if item in linked:
        cnt += 1

print(t+cnt+1)