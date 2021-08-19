# https://www.acmicpc.net/problem/8983

import sys
M, N, L = map(int, sys.stdin.readline().split())
gunshot_position = list(map(int, sys.stdin.readline().split()))
animals = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
gunshot_position.sort()

cnt = 0

for animal in animals:
    
    start_index = 0
    end_index = len(gunshot_position)-1

    while start_index <= end_index:
        mid_index = (start_index+end_index)//2
        mid_position = gunshot_position[mid_index]
        
        distance = abs(mid_position-animal[0])+animal[1]

        if distance <= L:
            cnt += 1
            break

        if animal[0] < mid_position:
            end_index = mid_index-1
        elif animal[0] > mid_position:
            start_index = mid_index+1
        elif animal[0] == mid_position:
            break
    
print(cnt)