# https://www.acmicpc.net/problem/2675

import sys

t = int(sys.stdin.readline())

for i in range(t):
    input_list = list(sys.stdin.readline().split())
    iter_num = int(input_list[0])
    input_str = input_list[1]

    tmp_lst = []
    for j in range(len(input_str)):
        for k in range(iter_num):
            tmp_lst.append(input_str[j])
    
    print("".join(tmp_lst))