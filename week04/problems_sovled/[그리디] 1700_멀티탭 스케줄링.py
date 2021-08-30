# https://www.acmicpc.net/problem/1700

import sys
N, M = map(int, sys.stdin.readline().split())
input_arr = list(map(int, sys.stdin.readline().split()))

plugged = []

cnt = 0

for i in range(M):
    
    check_lst = [0]*N
    order = 1

    if input_arr[i] in plugged:
        continue

    if len(plugged) < N:
        plugged.append(input_arr[i])
        continue

    for j in range(i+1, M):

         if input_arr[j] in plugged:
            index_num = plugged.index(input_arr[j])

            if check_lst[index_num] == 0:
                check_lst[index_num] = order
                order += 1

    if 0 in check_lst:
        target = check_lst.index(0)
        del plugged[target]
        plugged.append(input_arr[i])
        cnt += 1
    else:
        max_num = max(check_lst)
        target = check_lst.index(max_num)
        del plugged[target]
        plugged.append(input_arr[i])
        cnt += 1

print(cnt)