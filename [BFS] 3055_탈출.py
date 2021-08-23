# https://www.acmicpc.net/problem/3055

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
map_info = []
dochi_queue = deque()
water_queue = deque()
for i in range(R):
    temp = []
    row = sys.stdin.readline().strip()
    for j in range(len(row)): 
        if row[j] == 'S':
            dochi_queue.append([i, j])
        elif row[j] == '*':
            water_queue.append([i, j])
        temp.append(row[j])    
    map_info.append(temp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = None

while (dochi_queue):

    check_dochi = dochi_queue.popleft()
    d_x = check_dochi[0]
    d_y = check_dochi[1]

    check_water = water_queue.popleft()
    w_x = check_water[0]
    w_y = check_water[1]

    print(map_info[1][0])

    for i in range(4):
        new_d_x = d_x + dx[i]
        new_d_y = d_y + dy[i]

        if 0<= new_d_x <R and 0<= new_d_y <C:
            if map_info[new_d_x][new_d_y] == '.':
                if map_info[d_x][d_y] == 'S':
                    map_info[new_d_x][new_d_y] = 1
                else:
                    map_info[new_d_x][new_d_y] = map_info[d_x][d_y] + 1
                dochi_queue.append([new_d_x, new_d_y])
            elif map_info[new_d_x][new_d_y] == 'D':
                answer = map_info[d_x][d_y] + 1
                dochi_queue.clear()
                

    for i in range(4):
        new_w_x = w_x + dx[i]
        new_w_y = w_y + dy[i]

        if 0<= new_w_x <R and 0<= new_w_y <C:
            if map_info[new_w_x][new_w_y] != 'X' or map_info[new_w_x][new_w_y] != 'D':
                map_info[new_w_x][new_w_y] = '*'          
                if [new_w_x, new_w_y] in dochi_queue:
                    dochi_queue.remove([new_w_x, new_w_y])
                water_queue.append([new_w_x, new_w_y])
 
if answer == None:
     print("KAKTUS")
else:
    print(answer)
