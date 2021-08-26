# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

N = int(sys.stdin.readline())
house_info = []
for _ in range(N):
    temp_lst = []
    temp = sys.stdin.readline().strip()
    for i in range(N):
        temp_lst.append(int(temp[i]))
    house_info.append(temp_lst)

def bfs_function(house_info, start_node, visited):
    queue = deque()
    queue.append(start_node)

    cnt = 0
    
    while queue:
        node = queue.popleft()
        x = node[0]
        y = node[1]
        
        if visited[x][y] == 0:
            visited[x][y] = 1
            cnt += 1
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<N and 0<=ny<N and house_info[nx][ny] > 0 and visited[nx][ny] == 0:
                    queue.append([nx, ny])
    
    return cnt

visited = [ [0 for _ in range(N)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

complex = 0
number_of_house = []

for i in range(N):
    for j in range(N):

        if house_info[i][j] > 0 and visited[i][j] == 0:
            temp = bfs_function(house_info, [i, j], visited)
            number_of_house.append(temp)
            complex += 1

number_of_house.sort()

print(complex)
for item in number_of_house:
    print(item)
