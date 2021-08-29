# https://www.acmicpc.net/problem/14852

import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())

def dp_function(x, dp_table):

    dp_table[0][0] = 1 
    dp_table[0][1] = 2
    dp_table[0][2] = 7
    dp_table[1][2] = 0

    for i in range(3, x+1):
        dp_table[1][i] = (dp_table[0][i-3] + dp_table[1][i-1]) % 1000000007
        dp_table[0][i] = (3*dp_table[0][i-2] + 2*dp_table[0][i-1] + 2*dp_table[1][i]) % 1000000007

    return dp_table[0][x]

dp_table = []
for i in range(2):
    dp_table.append([-1]+[0]*(N+1))

print(dp_function(N, dp_table))