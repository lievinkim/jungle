# https://www.acmicpc.net/problem/2805

import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

left_value = 1
right_value = data[len(data)-1]

while left_value<=right_value:
    mid_value = (left_value+right_value)//2

    total = 0

    for tree in data:
        if tree >= mid_value:
            total += tree-mid_value

    if total >= m:
        left_value = mid_value + 1
    else:
        right_value = mid_value -1

print(right_value)
