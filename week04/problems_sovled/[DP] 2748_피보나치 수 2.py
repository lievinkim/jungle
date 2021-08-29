# https://www.acmicpc.net/problem/2748

import sys
N = int(sys.stdin.readline())

def dp_fibonacci(x, dp_table):
    if x == 1:
        dp_table[x] = 1
        return 1
    elif x == 2:
        dp_table[x] = 1
        return 1
    elif x == 3:
        dp_table[x] = 2
        return 2

    if dp_table[x] != 0:
        return dp_table[x]
    
    dp_table[x] = dp_fibonacci(x-1, dp_table) + dp_fibonacci(x-2, dp_table)
    
    return dp_table[x]

dp_table = [-1] + [0]*N
print(dp_fibonacci(N, dp_table))