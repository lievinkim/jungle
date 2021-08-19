# https://www.acmicpc.net/problem/2110


import sys
a, b = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(a)]
house.sort()

start = 1
end = house[-1] - house[0]
result = 0

while start <= end:

    mid = (start+end)//2
    last_installed = house[0]
    count = 1

    for i in range(1, a):    
        if house[i] >= last_installed+mid:
            count += 1
            last_installed = house[i]

    if count >= b:
        result = mid
        start = mid+1
    else:
        end = mid -1

print(result)