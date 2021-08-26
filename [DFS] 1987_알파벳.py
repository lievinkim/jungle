# https://www.acmicpc.net/problem/1987

# 세로 R칸, 가로 C칸
# 1행 1열 말 위치
# 말 상하좌우 이동 가능
# 알파벳 배치 / 같은 알파벳이 적힌 칸은 2번 지나갈 수 없음

import sys
vtl, hzl = map(int, sys.stdin.readline().split())
map_info = [list(map(str, sys.stdin.readline().strip())) for _ in range(vtl)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

stack = []
stack.append([0, 0, 0])
level = 0

history = []
answer = 0

while stack:
    check = stack.pop()
    x = check[0]
    y = check[1]
    level = check[2]
    
    if level < len(history):
        history = history[0:level]
    
    if map_info[x][y] not in history:
        history.append(map_info[x][y])
        answer = max(answer, level+1)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nlevel = level + 1

            if 0<= nx <vtl and 0<= ny <hzl:
                stack.append([nx, ny, nlevel])

print(answer)