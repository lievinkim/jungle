# https://www.acmicpc.net/problem/2573

import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

N, M = map(int, sys.stdin.readline().split())
map_info = []
for _ in range(N):
    map_info.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_function(map_info, node_position, visited):

    melting_info = defaultdict(int)

    x = node_position[0]
    y = node_position[1]

    visited[x][y] = 1

    # for i in range(4):
    #     nx = x + dx[i]
    #     ny = y + dy[i]

    #     if 0<=nx<N and 0<=ny<M:
    #         if map_info[nx][ny] != 0 and not visited[nx][ny]:
    #             dfs_function(map_info, [nx, ny], visited)
    #         elif map_info[nx][ny] == 0:
    #             melting_info[(x, y)] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<=M:
            if map_info[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs_function(map_info, [nx, ny], visited)
            elif map_info[nx][ny] == 0:
                melting_info[(x, y)] += 1

    return melting_info

# def bfs_function(map_info, node_position, visited):

#     melting_info = defaultdict(int)
#     queue = deque()
#     queue.append(node_position)

#     while queue:
#         x, y = queue.popleft()
#         visited[x][y] = 1

        # for i in range(4):
        #     nx = x + dx[i]
        #     ny = y + dy[i]

        #     if 0<=nx<N and 0<=ny<=M:
        #         if map_info[nx][ny] != 0 and not visited[nx][ny]:
        #             visited[nx][ny] = 1
        #             queue.append([nx, ny])
        #         elif map_info[nx][ny] == 0:
        #             melting_info[(x, y)] += 1

#     return melting_info

year = 0

while True:

    visited = [[0 for _ in range(M)] for _ in range(N)]
    continent = 0

    for i in range(N):
        for j in range(M):
            if map_info[i][j] != 0 and not visited[i][j]:
                melting_info = dfs_function(map_info, [i, j], visited)
                continent += 1

    if continent > 1:
        print(year)
        sys.exit()
    
    if continent == 0:
        print(0)
        sys.exit()

    for (x, y), cnt in melting_info.items():
        map_info[x][y] = 0 if map_info[x][y] < cnt else map_info[x][y]-cnt

    year += 1