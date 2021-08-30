# https://www.acmicpc.net/problem/1931

import sys
N = int(sys.stdin.readline())

input_arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    input_arr.append([a, b])

input_arr.sort(key= lambda x: (x[1], x[0]))

cnt = 1
endtime = input_arr[0][1]

for i in range(1, N):

    if input_arr[i][0] >= endtime:
        cnt += 1
        endtime = input_arr[i][1]

print(cnt)