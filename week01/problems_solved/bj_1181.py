# https://www.acmicpc.net/problem/1181
# 삽입정렬 시도 (시간초과 실패)
# 병합정렬 시도 (성공)

# 병합정렬
import sys

t = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(0, t)]

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):

        if len(low_arr[l]) < len(high_arr[h]):
            merged_arr.append(low_arr[l])
            l += 1
        elif len(low_arr[l]) > len(high_arr[h]):
            merged_arr.append(high_arr[h])
            h += 1
        else:
            if low_arr[l] == high_arr[h]:     
                high_arr.remove(high_arr[h])
            else:
                for k in range(0, len(low_arr[l])):
                    if low_arr[l][k] < high_arr[h][k]:
                        merged_arr.append(low_arr[l])
                        l += 1
                        break
                    elif low_arr[l][k] > high_arr[h][k]:
                        merged_arr.append(high_arr[h])
                        h += 1
                        break

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr

for item in merge_sort(data):
    print(item)

# 삽입 정렬
# cnt = 0
# for i in range(1, len(data)):
#     if i >= len(data)-cnt:
#         break
    
#     i = i-cnt

#     for j in range(0, i):
#         if len(data[i]) < len(data[j]):
#             temp = data[j]
#             data[j] = data[i]
#             data[i] = temp
#         elif len(data[i]) == len(data[j]):
#             if data[i] == data[j]:
#                 data.pop(i)
#                 cnt += 1
#                 break
#             for k in range(0, len(data[i])):
#                 if data[i][k] < data[j][k]:
#                     temp = data[j]
#                     data[j] = data[i]
#                     data[i] = temp
# for item in data:
#     print(item)