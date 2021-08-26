# https://www.acmicpc.net/problem/1697

import sys
N, K = map(int, sys.stdin.readline().split())

time = 0

while K//N >= 2:
    N = 2*N
    time += 1

subin_position = N
target_position = K






distance = abs(N-K)

# 순간이동 조건

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