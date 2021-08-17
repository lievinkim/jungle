# https://www.acmicpc.net/problem/9498

import sys

point = int(sys.stdin.readline())

if 90 <= point <= 100:
    print("A")
elif 80 <= point <= 89:
    print("B")
elif 70 <= point <= 79:
    print("C")
elif 60 <= point <= 69:
    print("D")
else:
    print("F") 