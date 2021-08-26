# https://www.acmicpc.net/problem/2617

import sys
a, b = map(int, sys.stdin.readline().split())
data = []
for _ in range(b):
    data.append(list(map(int, sys.stdin.readline().split())))

lighter = [[] for _ in range(a+1)]

for i in range(b):
    x = data[i][0]
    y = data[i][1]
    lighter[x].append(y)

print(heavy) 


