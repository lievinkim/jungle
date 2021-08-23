# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

computer_num = int(sys.stdin.readline())
edge_num = int(sys.stdin.readline())
edge_info = [list(map(int, sys.stdin.readline().split())) for _ in range(edge_num)]

def dfs_function(adjacent_lst:list, starting_node:int):
    stack = [starting_node]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for i in range(len(adjacent_lst[node])):
                stack.append(adjacent_lst[node][i])

    print(len(visited)-1)

def bfs_function(adjacent_lst:list, starting_node:int):

    queue = deque()
    queue.append(starting_node)
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for i in range(len(adjacent_lst[node])):
                queue.append(adjacent_lst[node][i])

    print(len(visited)-1)

adjacent_lst = [[] for _ in range(computer_num+1)]
for item in edge_info:
    adjacent_lst[item[0]].append(item[1])
    adjacent_lst[item[1]].append(item[0])

dfs_function(adjacent_lst, 1)
bfs_function(adjacent_lst, 1)

def dfs_function_recur(adjacent_lst:list, visited:list, starting_node:int):

    visited[starting_node] = True

    for node in adjacent_lst[starting_node]:
        if not visited[node]:
            dfs_function_recur(adjacent_lst, visited, node)


    return visited

visited_before = [False]*(computer_num+1)
visited_after = dfs_function_recur(adjacent_lst, visited_before, 1)

cnt = 0

for i in visited_after:
    if i == True:
        cnt += 1

print(cnt-1)