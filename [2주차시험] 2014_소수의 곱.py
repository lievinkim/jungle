# https://www.acmicpc.net/problem/2014

import sys
import heapq
K, N = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

heap = []
for i in range(K):
    heapq.heappush(heap, data[i])





# while len(heap) <= N:
#     for i in range(len(heap)):
#         for j in range(i, len(heap), 1):
#             new_num = heap[i]*heap[j]
#             if new_num not in heap:
#                 heapq.heappush(heap, new_num)
#                 heap.sort()
#                 break
#         break

# print(heap)







# while len(heap) <= N:

#     x = heap[0]
#     y = min(heap[1], heap[2])
#     new_num = x*y
#     heapq.heappush(heap, new_num)

# print(heap)

