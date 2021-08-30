# https://www.acmicpc.net/problem/1946

import sys
T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())
    input_arr = []
    for i in range(N):
        input_arr.append(list(map(int, sys.stdin.readline().split())))
    input_arr.sort(key = lambda x: (x[0]))

    count = 1
    score = input_arr[0][1]

    for i in range(1, N):

        if input_arr[i][1] < score:
            count += 1
            score = input_arr[i][1]
    
    print(count)
