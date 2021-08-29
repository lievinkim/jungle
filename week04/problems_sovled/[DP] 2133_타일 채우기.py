# https://www.acmicpc.net/problem/2133

import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())

def dp(width, dp_table):

    if width == 0:
        return 1
    elif width == 1:
        return 0
    elif width == 2:
        return 3
    elif dp_table[width] != 0:
        return dp_table[width]
    
    result = 3 * dp(width-2, dp_table)

    for i in range(3, width+1):
        if (i%2 == 0):
            result += 2*dp(width-i, dp_table)
    
    dp_table[width] = result

    return dp_table[width]

dp_table = [-1] + [0]*N

print(dp(N, dp_table))