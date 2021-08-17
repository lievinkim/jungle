# https://www.acmicpc.net/problem/2577

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

answer = str(a*b*c)

for i in range(10):
    print(answer.count(str(i)))