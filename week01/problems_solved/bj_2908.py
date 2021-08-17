# https://www.acmicpc.net/problem/2908

import sys

a, b = map(int, sys.stdin.readline().split())
str_a = str(a)
reversed_str_a = str_a[::-1]
str_b = str(b)
reversed_str_b = str_b[::-1]

changed_a = int(reversed_str_a)
changed_b = int(reversed_str_b)

if changed_a > changed_b:
    print(changed_a)
else:
    print(changed_b)



