# https://www.acmicpc.net/problem/1967

import sys
from collections import deque

sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())
adjacent_lst = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    adjacent_lst[a].append([b, c])

def dfs_function(adjacent_lst, start_node, visited, distance=0):
    global answer

    visited.append(start_node[0])
    distance += start_node[1]

    answer = max(answer, distance)

    for node in adjacent_lst[start_node[0]]:
        if node[0] not in visited:
            dfs_function(adjacent_lst, node, visited, distance)

answer = 0
visited = []
dfs_function(adjacent_lst, [8, 0], visited)
print(answer)

# for i in range(1, N+1):
#     answer = 0
#     visited = []
#     start_node = [i, 0]
#     dfs_function(adjacent_lst, start_node, visited)
#     print(answer)