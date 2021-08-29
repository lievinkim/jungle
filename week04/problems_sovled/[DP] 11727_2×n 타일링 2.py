# https://www.acmicpc.net/problem/11727

import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())

def dp(width, dp_table):
    
    if width == 1:
        return 1
    elif width == 2:
        return 3
    elif dp_table[width] != 0:
        return dp_table[width]

    dp_table[width] = (dp(width-1, dp_table)+dp(width-2, dp_table)*2) % 10007
    
    return dp_table[width]

dp_table = [-1] + [0]*N

print(dp(N, dp_table))