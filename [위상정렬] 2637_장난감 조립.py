# https://www.acmicpc.net/problem/2637

# 기본 부품과 중간 부품
# 기본 부품은 다른 부품을 사용하여 조립 불가
# 중간 부품은 다른 부품을 사용하여 조립 가능
# 예시
# 기본 부품 1, 2, 3, 4
# 중간 부품 5 = 기본 부품 1 2개 + 기본 부품 2 2개
# 중간 부품 6 = 중간 부품 5 2개 + 기본 부품 3 3개 + 기본 부품 4 4개
# 완제품 7 = 중간 부품 5 2개 + 중간 부품 6 3개 + 기본 부품 4 4개
# 필요한 부품은 기본 부품 1 16개 + 기본 부품 2 16개 + 기본 부품 3 9개 + 기본 부품 4 17개
# 필요한 기본 부품의 종류별 개수 구하기

import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
input_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
in_degree = [-1] + [0]*N
graph = [[] for _ in range(N+1)]

basic = []
for i in range(1, N+1):
    basic.append(i)

for item in input_arr:
    x = item[0]
    y = item[1]
    z = item[2]
    in_degree[y] += 1
    graph[x].append([y, z])
    if x in basic:
        basic.remove(x)

queue = deque()

for i in range(N, -1, -1):
    queue.append(i)

answer = [-1] + [0]*(N-1) + [1]

while queue:

    check = queue.popleft()

    for i in range(len(graph[check])):
        module_num = graph[check][i][0]
        module_cnt = graph[check][i][1]
        answer[module_num] += answer[check]*module_cnt

for i in range(1, N+1):
    if i in basic:
        print(f'{i} {answer[i]}')