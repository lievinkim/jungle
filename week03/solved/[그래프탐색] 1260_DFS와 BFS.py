# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())

data = []
for _ in range(M):
    data.append(list(map(int, sys.stdin.readline().split())))

adjacent_lst = [[] for _ in range(N+1)]
for item in data:
    adjacent_lst[item[0]].append(item[1])
    adjacent_lst[item[1]].append(item[0])

def dfs_function(adjacent_lst, start_node):
    
    stack = [start_node]
    visited = []

    while len(stack) != 0:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            adjacent_lst[node].sort()
            adjacent_lst[node].reverse()

            for i in range(len(adjacent_lst[node])):
                stack.append(adjacent_lst[node][i])
    
    print(" ".join(str(x) for x in visited))

def bfs_function(adjacent_lst, start_node):

    queue = deque()
    queue.append(start_node)
    visited = []

    while len(queue) != 0:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            adjacent_lst[node].sort()
            
            for i in range(len(adjacent_lst[node])):
                queue.append(adjacent_lst[node][i])

    print(" ".join(str(x) for x in visited))
        
dfs_function(adjacent_lst, V)
bfs_function(adjacent_lst, V)




# def dfs_function()