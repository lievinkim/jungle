# https://www.acmicpc.net/problem/2750

import sys
t = int(sys.stdin.readline())

data = []

def insertion_sort(n):
    global data

    for i in range(n):
        data.append(int(sys.stdin.readline()))
    
    for j in range (1, len(data)):
        for k in range (j):
            if data[j] < data[k]:
                temp = data[j]
                data[j] = data[k]
                data[k] = temp

def binary_insertion_sort(n):
    global data

    for i in range(n):
        data.append(int(sys.stdin.readline()))

    for j in range(1, len(data)):
        key = data[j]
        pl = 0
        pr = j-1

        while True:
            pc = (pl+pr)//2
            if key < data[pc]:
                pr = pc - 1
            elif key > data[pc]:
                pl = pc + 1
            if pl > pr:
                break
        
        pd = pr + 1

        for k in range(j, pd, -1):
            data[k] = data[k-1]
        
        data[pd] = key
        
# insertion_sort(t)
binary_insertion_sort(t)

for item in data:
    print(item)