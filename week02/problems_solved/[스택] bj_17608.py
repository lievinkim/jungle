# https://www.acmicpc.net/problem/17608

import sys

t = int(sys.stdin.readline())
data = []
for _ in range(0, t):
    data.append(int(sys.stdin.readline()))

visible_bar = 0
max_height = 0

for i in range(t-1, -1, -1):
    if data[i] > max_height:
        visible_bar += 1
        max_height = data[i]

print(visible_bar)