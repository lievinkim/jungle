# https://www.acmicpc.net/problem/1110

import sys
sys.setrecursionlimit(10**8)

t = int(sys.stdin.readline())
cnt = 0

def generate_new_number(first, n, cnt):

    if n<10:
        n = str(n).zfill(2)
    else:
        n = str(n)

    bridge_num = int(n[0])+int(n[1])

    if bridge_num < 10:
        bridge_num = str(bridge_num).zfill(2)
    else:
        bridge_num = str(bridge_num)

    new_num = int(n[1]+bridge_num[1])
    cnt += 1

    if new_num == first:
        return cnt
    else :
        cnt = generate_new_number(first, new_num, cnt)
        return cnt

answer = generate_new_number(t, t, cnt)
print(answer)