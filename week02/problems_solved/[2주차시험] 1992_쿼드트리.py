# https://www.acmicpc.net/problem/1992

import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    temp = []
    x = sys.stdin.readline().strip()
    for i in range(len(x)):
        temp.append(int(x[i]))
    data.append(temp)

answer = []

def solution(x, y, N):
    global answer

    color = data[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if data[i][j] != color:
                answer.append("(")
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                answer.append(")")
                return

    if color == 0:
        answer.append("0")
    else:
        answer.append("1")


solution(0, 0, n)
print("".join(answer))