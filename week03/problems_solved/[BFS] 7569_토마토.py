# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

# 입력 정보 받기

M, N, H = map(int, sys.stdin.readline().split())
tomato_info = []
queue = deque([])

for h in range(H):
    temp = []
    for x in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for y in range(M):
            if temp[x][y] == 1:
                queue.append([h, x, y])
    tomato_info.append(temp)

dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

while (queue):
    h, x, y = queue.popleft()

    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nh < H and 0<= nx < N and 0 <= ny < M and tomato_info[nh][nx][ny] == 0:
            queue.append([nh, nx, ny])
            tomato_info[nh][nx][ny] = tomato_info[h][x][y] + 1

day = 0
for i in tomato_info:
    for j in i:
        for k in j:        
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
        
print(day-1)