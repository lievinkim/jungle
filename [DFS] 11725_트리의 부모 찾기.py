# https://www.acmicpc.net/problem/11725

import sys

number_of_nodes = int(sys.stdin.readline())
parent_info = [1, 1]+[0]*(number_of_nodes-1)

node_info = []
stack = []

for i in range(number_of_nodes-1):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1 or b == 1 :
        stack.append([a, b])
    else:
        node_info.append([a, b])

while stack:

    num = stack.pop()
    x = num[0]
    y = num[1]

    if parent_info[x] != 0 and parent_info[y] == 0:
        parent_info[y] = x
        for item in node_info:
            if item[0] == y or item[1] == y:
                stack.append(item)
                node_info.remove(item)
    elif parent_info[x] == 0 and parent_info[y] != 0:
        parent_info[x] = y
        for item in node_info:
            if item[0] == x or item[1] == x:
                stack.append(item)
                node_info.remove(item)
    elif parent_info[x] == 0 and parent_info[y] == 0:
        node_info.append([x, y])

for i in range(2, number_of_nodes+1):
    print(parent_info[i])
        




# data = [list(map(int, sys.stdin.readline().split())) for _ in range(number_of_nodes-1)]

