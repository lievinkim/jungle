# https://www.acmicpc.net/problem/2753
# 윤년은 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
import sys

year = int(sys.stdin.readline())

if year%4 == 0:
    if year%100 != 0 or year%400==0:
        print(1)
    else:
        print(0)
else:
    print(0)