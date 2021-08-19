# https://www.acmicpc.net/problem/2630

import sys
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

white = 0
blue = 0

def solution(x, y, N):
    global white, blue, A
    color = A[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if A[i][j] != color:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

solution(0, 0, N)
print(white)
print(blue)