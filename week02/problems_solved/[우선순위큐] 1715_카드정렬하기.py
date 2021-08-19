# https://www.acmicpc.net/problem/1715

import sys
import heapq

t = int(sys.stdin.readline())
heap = []
for _ in range(t):
    x = int(sys.stdin.readline())
    heapq.heappush(heap, x)

cnt = 0
for i in range(t-1):

    if len(heap) <= 2:
        for num in heap:
            cnt += num
        break

    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    
    new_num = a + b
    cnt += new_num
    heapq.heappush(heap, new_num)

print(cnt)