# https://www.acmicpc.net/problem/2261

import sys
n = int(sys.stdin.readline())
positions = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(positions)