# https://www.acmicpc.net/problem/10872

import sys

t = int(sys.stdin.readline())

def factCal(n):

    if n == 0:
        return 1
    else:
        return n*factCal(n-1)
    
print(factCal(t))