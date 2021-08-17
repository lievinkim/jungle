# https://www.acmicpc.net/problem/10871

import sys

n, x= map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

for num in lst:
    if num < x:
        print(num)   