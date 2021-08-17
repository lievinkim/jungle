# https://www.acmicpc.net/problem/2493

import sys

t = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

compared_stack = [[0,0]]
ans = []

for i in range(0, t):

    for j in range(len(compared_stack)-1, -1, -1):
        if data[i] < compared_stack[j][0]:
            compared_stack.append([data[i], i])
            ans.append(compared_stack[j][1]+1)
            break
        elif data[i] > compared_stack[j][0]:
            del(compared_stack[j])
    
    if len(compared_stack) == 0:
        compared_stack.append([data[i], i])
        ans.append(0)

print(" ".join(map(str, ans)))

# for i in range(1, t):
#     temp = 0
#     for j in range(i-1, -1, -1):
#         if data[i]-data[j] < 0:
#             temp = j+1
#             break
    
#     ans.append(temp)

# print(" ".join(map(str, ans)))
