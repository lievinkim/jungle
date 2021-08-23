# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
path_info = []
for _ in range(N):
    temp = []
    x = sys.stdin.readline().strip()
    for i in range(len(x)):
        temp.append(int(x[i]))
    path_info.append(temp)

queue = deque()
visited_info = [[0]*M for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue.append([0, 0])
visited_info[0][0] = 1

while queue:

    check_queue = queue.popleft()
    x = check_queue[0]
    y = check_queue[1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            
            if visited_info[nx][ny] == 0 and path_info[nx][ny] == 1:
                visited_info[nx][ny] = visited_info[x][y] + 1
                queue.append([nx, ny])

print(visited_info[N-1][M-1])