# https://www.acmicpc.net/problem/2252

import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
input_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]


# BFS와 In-Degree를 이용한 위상 정렬

in_degree = [-1]+[0]*N

for item in input_arr:
    x = item[0]
    y = item[1]
    in_degree[y] += 1
    graph[x].append(y)

queue = deque()

for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

answer = []

while queue:
    check = queue.popleft()
    # if check not in answer: 
    answer.append(check)

    for i in graph[check]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)

print(*answer)


# DFS(재귀함수)를 이용한 위상 정렬

visited = [-1]+[0]*N
answer = []

def top_by_recursion(starting_node):

    visited[starting_node] = 1

    for node in graph[starting_node]:
        if visited[node] == 0:
            top_by_recursion(node)
    
    answer.append(starting_node)

for i in range(1, N+1):
    if visited[i] == 0:
        top_by_recursion(i)     

print(*list(reversed(answer)))

