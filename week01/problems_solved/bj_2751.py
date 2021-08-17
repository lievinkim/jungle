# https://www.acmicpc.net/problem/2751

import sys

t = int(sys.stdin.readline())
data = []
for i in range(0, t):
        data.append(int(sys.stdin.readline()))

def merge_sort(arr):

    if len(arr) < 2:
        return arr

    middle = len(arr)//2
    low_arr = merge_sort(arr[:middle])
    high_arr = merge_sort(arr[middle:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        elif low_arr[l] > high_arr[h]:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

for item in merge_sort(data):
    print(item)





# def merge_sort(data):
    
#     if len(data) < 2:
#         return data

#     mid = len(data) // 2
#     low_data = merge_sort(data[:mid])
#     high_data = merge_sort(data[mid:])

#     merged_data = []
#     l = h = 0
#     while l < len(low_data) and h < len(high_data):
#         if low_data[l] < high_data[h]:
#             merged_data.append(low_data[l])
#             l += 1
#         else:
#             merged_data.append(high_data[h])
#             h += 1
#     merged_data += low_data[l:]
#     merged_data += high_data[h:]
#     return merged_data
    
# for i in merge_sort(data):
#     print(str(i))
