# https://www.acmicpc.net/problem/2869

import sys

a, b, c = map(int, sys.stdin.readline().split())
day_count = 1
left_length = c-a
possible_length = a-b

if (left_length%possible_length == 0):
    print(day_count+(left_length//possible_length))
else:
    print(day_count+(left_length//possible_length)+1)