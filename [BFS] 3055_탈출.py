# https://www.acmicpc.net/problem/3055

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
map_info = []
queue = deque()
cnt = 0
for i in range(0, R):
    temp = []
    row = sys.stdin.readline().strip()
    for j in range(0, len(row)):
        if row[j] == 'S':
            temp.append(0)
            queue.appendleft([i, j, row[j]])
            cnt += 1
            temp.append(0)
            continue
        elif row[j] == '*':
            queue.append([i, j, row[j]])
        temp.append(row[j])
    map_info.append(temp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while cnt > 0:

    check_queue = queue.popleft()
    x = check_queue[0]
    y = check_queue[1]     

    if check_queue[2] == 'S':
        cnt -= 1

        for i in range(4):
            new_d_x = x + dx[i]
            new_d_y = y + dy[i]

            if 0 <= new_d_x < R and 0 <= new_d_y < C:
                if map_info[new_d_x][new_d_y] == '.':
                    map_info[new_d_x][new_d_y] = map_info[x][y] + 1    
                    queue.append([new_d_x, new_d_y, 'S'])
                    cnt += 1
                elif map_info[new_d_x][new_d_y] == 'D':
                    answer = map_info[x][y] + 1
                    print(answer)
                    sys.exit()

    else:

        for i in range(4):
            new_w_x = x + dx[i]
            new_w_y = y + dy[i]

            if 0 <= new_w_x < R and 0 <= new_w_y < C:
                if map_info[new_w_x][new_w_y] != 'X' and map_info[new_w_x][new_w_y] != 'D':
                    map_info[new_w_x][new_w_y] = '*'
                    queue.append([new_w_x, new_w_y, '*'])
                    if [new_w_x, new_w_y, 'S'] in queue:
                        queue.remove([new_w_x, new_w_y, 'S'])
                        cnt -= 1


print("KAKTUS")