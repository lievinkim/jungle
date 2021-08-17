# https://www.acmicpc.net/problem/10828

import sys
t = int(sys.stdin.readline())
data = []
for i in range(0, t):
    data.append(sys.stdin.readline().split())

arr = []

def push(arr, n):
    arr.append(n)
    return arr

def pop(arr):
    if len(arr) == 0:
        print(-1)
        return
    print(arr[len(arr)-1])
    arr.pop(len(arr)-1)
    return

def size(arr):
    print(len(arr))
    return

def empty(arr):
    if len(arr) == 0:
        print(1)
        return
    print(0)
    return

def top(arr):
    if len(arr) == 0:
        print(-1)
        return
    print(arr[len(arr)-1])
    return

for i in range(0, t):

    if data[i][0] == 'push':
        arr = push(arr, data[i][1])
    elif data[i][0] == 'pop':
        pop(arr)
    elif data[i][0] == 'size':
        size(arr)
    elif data[i][0] == 'empty':
        empty(arr)
    elif data[i][0] == 'top':
        top(arr)