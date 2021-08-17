# https://www.acmicpc.net/problem/18258

import sys
t = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(t)]

queue = []
front = 0

for i in range(0, t):
    if arr[i][0] == "push":
        queue.append(arr[i][1])
    elif arr[i][0] == "pop":
        if len(queue)-front > 0:
            print(queue[front])
            front += 1
        else:
            print(-1)
    elif arr[i][0] == "size":
        print(len(queue)-front)
    elif arr[i][0] == "empty":
        if len(queue)-front == 0:
            print(1)
        else:
            print(0)
    elif arr[i][0] == "front":
        if len(queue)-front > 0:
            print(queue[front])
        else:
            print(-1)
    elif arr[i][0] == "back":
        if len(queue)-front > 0:
            print(queue[len(queue)-1])
        else:
            print(-1)