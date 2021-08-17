# https://www.acmicpc.net/problem/1085

import sys
from math import *

x, y, w, h = map(int, sys.stdin.readline().split())
min_w_length = 0
min_h_length = 0

# min_w_length
if (w-x) < (w/2):
    min_w_length = w-x
else:
    min_w_length = x

# min_h_length
if (h-y) < (h/2):
    min_h_length = h-y
else:
    min_h_length = y

if (min_w_length < min_h_length):
    print(min_w_length)
else:
    print(min_h_length)