# https://www.acmicpc.net/problem/1904

import sys

N = int(sys.stdin.readline())
dp_table = [-1] + [0]*(N+1)

dp_table[1] = 1
dp_table[2] = 2

for i in range(3, N+1):
    dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 15746

print(dp_table[N])


# def dp_function(x, dp_table):
    
#     if dp_table[x] != 0:
#         return dp_table[x]

#     dp_table[x] = dp_function(x-1, dp_table) % 15746 + dp_function(x-2, dp_table) % 15746

#     return dp_table[x]

# print(dp_function(N, dp_table))