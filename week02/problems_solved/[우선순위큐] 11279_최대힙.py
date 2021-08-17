# https://www.acmicpc.net/problem/11279

import sys

def down_heap(a, root:int, last:int) -> None:
    temp = a[root]
    parent = root
    while parent < (last+1)//2:
        cl = parent*2+1
        cr = cl+1
        child = cr if cr <= last and a[cr]>a[cl] else cl
        if temp >= a[child]:
            break
        a[parent] = a[child]
        parent = child
    a[parent] = temp

def insert_heap(a, value:int) -> None:
    a.append(value)
    current_index = len(a)-1
    while current_index > 0:
        parent_index = (current_index-1)//2
        if a[parent_index] > a[current_index]:
            break
        else:
            a[current_index] = a[parent_index]
            a[parent_index] = value
            current_index = parent_index

t = int(sys.stdin.readline())

heap_lst = []
cnt = 0

for _ in range(t):
    x = int(sys.stdin.readline())
    if x == 0:
        if cnt == 0:
            print(0)
        else:
            print(heap_lst[0])

            if cnt == 1:
                del heap_lst[0]
                cnt -= 1
            else:
                heap_lst[0] = heap_lst[cnt-1]
                del heap_lst[cnt-1]
                cnt -= 1
                down_heap(heap_lst, 0, cnt-1)
    else:
        insert_heap(heap_lst, x)
        cnt += 1

    
    