# https://www.acmicpc.net/problem/13334

import sys
import heapq

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
d = int(sys.stdin.readline())

roads = []
for item in data:
    if abs(item[0]-item[1]) <= d:
        roads.append(sorted(item))
roads.sort(key=lambda x: x[1])

heap = []
max_n = 0

for road in roads:

    current_end = road[1]
    current_start = road[1]-d

    if not heap:
        heapq.heappush
    
    for started in heap:
        if started < current_start:
            heapq.heappop(heap)
        else:
            break

    if road[0] >= current_start:
        heapq.heappush(heap, road[0])

    max_n = max(max_n, len(heap))

print(max_n)
    
