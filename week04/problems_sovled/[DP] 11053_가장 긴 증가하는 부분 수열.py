# https://www.acmicpc.net/problem/11053

import sys
N = int(sys.stdin.readline())
input_arr = list(map(int, sys.stdin.readline().split()))

dp_table = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if input_arr[i] > input_arr[j]:
            dp_table[i] = max(dp_table[i], dp_table[j]+1)

print(max(dp_table))

