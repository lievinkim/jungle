# https://www.acmicpc.net/problem/1978

import sys
t = int(sys.stdin.readline())
input_lst = list(map(int, sys.stdin.readline().split()))

cnt = 0

if 1 in input_lst:
    input_lst.remove(1)
if 2 in input_lst:
    input_lst.remove(2)
    cnt += 1
if 3 in input_lst:
    input_lst.remove(3)
    cnt += 1

for i in range(2, 501):
    tmp_lst = []
    for j in range(int(1000/i)):
        tmp_lst.append(i*(j+2))
    input_lst = list(set(input_lst).difference(tmp_lst))

print(cnt+len(input_lst))