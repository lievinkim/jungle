# https://www.acmicpc.net/problem/2739

import sys

n = int(sys.stdin.readline())

for i in range(9):
    print("{0} * {1} = {2}".format(n, i+1, n*(i+1)))