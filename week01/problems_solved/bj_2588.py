# https://www.acmicpc.net/problem/2588

import sys

a,b = map(int, sys.stdin.readline().split())

# b를 10의 자리수로 나누기
b1 = int(b/1)%10
b2 = int(b/10)%10
b3 = int(b/100)%10

print(a*b1)
print(a*b2)
print(a*b3)
print(a*b)