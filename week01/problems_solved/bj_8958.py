# https://www.acmicpc.net/problem/8958

import sys

t = int(sys.stdin.readline())

for i in range(t):
    tmp_str = sys.stdin.readline()
    tmp_lst = []
    score = 0
    cnt = 0

    for j in tmp_str:
        tmp_lst.append(j)
    
    for k in range(len(tmp_lst)):
        if tmp_lst[k] == 'O':
            score = score + 1 + cnt
            cnt += 1
        else:
            cnt = 0
    
    print(score)
