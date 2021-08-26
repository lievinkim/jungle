# https://www.acmicpc.net/problem/2573

import sys
from collections import deque

vtl, hzl = map(int, sys.stdin.readline().split())
map_info = []
ice_info = []
for i in range(vtl):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(hzl):
        if temp[j] != 0:
            ice_info.append([i, j])
    map_info.append(temp)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs_function(map_info:list, starting_node:list):

    queue = deque()
    queue.append(starting_node)
    
    check = set()
    cnt = 0

    while queue:

        temp_num = queue.popleft()
        check.add(temp_num)
        print(check)
        cnt += 1
        x = temp_num[0]
        y = temp_num[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<= new_x <vtl and 0<= new_y <hzl and map_info[new_x][new_y] > 0 and [new_x, new_y] not in check:
                queue.append([new_x, new_y])
    
    return cnt

answer = 0
temp_lst = []

while (ice_info):

    answer += 1

    for item in temp_lst:
        map_info[item[0]][item[1]] = 0

    for i in range(vtl):
        for j in range(hzl):

            if map_info[i][j] == 0:
                for k in range(4):
                    new_x = i + dx[k]
                    new_y = j + dy[k]

                    if 0<= new_x < vtl and 0<= new_y <hzl and map_info[new_x][new_y] > 0:
                        map_info[new_x][new_y] -= 1
                        if map_info[new_x][new_y] == 0:
                            ice_info.remove([new_x, new_y])
                            map_info[new_x][new_y] = -1
                            temp_lst.append([new_x, new_y])
                            
    
    temp = bfs_function(map_info, ice_info[0])

    if len(ice_info) != temp:
        print(answer)
        sys.exit()

print(0)





