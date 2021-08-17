# https://www.acmicpc.net/problem/1655

import sys
t = int(sys.stdin.readline())

# make two heaps (left - max heap, right - min heap)
left_heap = []
right_heap = []

def insert_heap_max(arr:list, value:int) -> None:
    arr.append(value)
    current_index = len(arr)-1

    while current_index > 0:
        parent_index = (current_index-1)//2
        if arr[current_index] < arr[parent_index]:
            break
        arr[current_index] = arr[parent_index]
        arr[parent_index] = value
        current_index = parent_index

def insert_heap_min(arr:list, value:int) -> None:
    arr.append(value)
    current_index = len(arr)-1

    while current_index > 0:
        parent_index = (current_index-1)//2
        if arr[current_index] > arr[parent_index]:
            break
        arr[current_index] = arr[parent_index]
        arr[parent_index] = value
        current_index = parent_index

def heap_max(arr, root:int, last:int) -> None:
    temp = arr[root]
    
    parent = root
    while parent < (last+1)//2:
        cl = parent * 2 + 1
        cr = cl + 1
        child = cr if cr <= last and arr[cr] > arr[cl] else cl
        if temp >= arr[child]:
            break
        arr[parent] = arr[child]
        parent = child
    arr[parent] = temp

def heap_min(arr, root:int, last:int) -> None:
    temp = arr[root]
    
    parent = root
    while parent < (last+1)//2:
        cl = parent * 2 + 1
        cr = cl + 1
        child = cr if cr <= last and arr[cr] < arr[cl] else cl
        if temp <= arr[child]:
            break
        arr[parent] = arr[child]
        parent = child
    arr[parent] = temp

data = [int(sys.stdin.readline()) for _ in range(t)]
for x in data:
    
    if len(left_heap) <= len(right_heap):
        insert_heap_max(left_heap, x)
        heap_max(left_heap, 0, len(left_heap)-1)
        if len(right_heap) != 0:
            if right_heap[0] <= left_heap[0]:
                temp = right_heap[0]
                right_heap[0] = left_heap[0]
                left_heap[0] = temp
                heap_max(left_heap, 0, len(left_heap)-1)
                heap_min(right_heap, 0, len(right_heap)-1)
        
    elif len(left_heap) > len(right_heap):
        insert_heap_min(right_heap, x)
        heap_min(right_heap, 0, len(right_heap)-1)
        if right_heap[0] <= left_heap[0]:
            temp = right_heap[0]
            right_heap[0] = left_heap[0]
            left_heap[0] = temp
            heap_max(left_heap, 0, len(left_heap)-1)
            heap_min(right_heap, 0, len(right_heap)-1)
 
    print(left_heap[0])