# https://www.acmicpc.net/problem/1914

import sys

t = int(sys.stdin.readline())

def hanoiTower(n, a, b, c):
    global move
    if n == 1:
        print(a, c)
    else:
        hanoiTower(n-1, a, c, b)
        print(a, c)
        hanoiTower(n-1, b, a, c)

if (t<=20):
    print(2**t-1)
    hanoiTower(t, 1, 2, 3)
else:
    print(2**t-1)
