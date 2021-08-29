# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adjacent_lst = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjacent_lst[a].append(b)
    adjacent_lst[b].append(a)

def dfs_iteration(graph, start):

    visited = []
    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    
    print(len(visited)-1)

def dfs_recursion(graph, start, visited=[]):

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursion(graph, node, visited)

    return len(visited)-1

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

# dfs_iteration(adjacent_lst, 1)
print(dfs_recursion(adjacent_lst, 1))
