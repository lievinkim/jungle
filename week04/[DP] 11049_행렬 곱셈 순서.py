# https://www.acmicpc.net/problem/11049

import sys
N = int(sys.stdin.readline())

matrix = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    matrix.append((a,b))

dp_table = [[-1]*N for _ in range(N)]

def dp_matrix_chain(x, y, dp_table, matrix):

    if dp_table[x][y] != -1:
        return dp_table[x][y]

    if x == y:
        return 0
    
    if x + 1 == y:
        return matrix[x][0] * matrix[x][1] * matrix[y][1]
    
    for i in range(x, y):
        left = dp_matrix_chain[x, i, dp_table, matrix]
        bottom = dp_matrix_chain[i+1, x, dp_table, matrix]
        if dp_table[x][y] == -1 or dp_table[x][y] < left + bottom + matrix[x][0]*matrix[i][1]*matrix[y][1]:
            dp_table[x][y] = left + bottom + matrix[x][0]*matrix[i][1]*matrix[y][1]
        
    return dp_table[x][y]

print(dp_matrix_chain(0, N-1, dp_table, matrix))