# https://www.acmicpc.net/problem/2628

import sys

width, height = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

# data
# [[0, 3], [1, 4], [0, 2]]

width_cut = [0, width]
height_cut = [0, height]

 
for j in range(len(data)):
    if data[j][0] != 0:
        width_cut.append(data[j][1])
    else:
        height_cut.append(data[j][1])

width_cut.sort()
height_cut.sort()

def cal_maxlength(a: list):
    max_legnth = 0
    for i in range(len(a)-1):
        if(a[i+1]-a[i])>max_legnth:
            max_legnth = a[i+1]-a[i]
    return max_legnth

print(cal_maxlength(width_cut)*cal_maxlength(height_cut))

# for w in range(len(width_cut)-1):
#     if (width_cut[w+1]-width_cut[w]) > max_width:
#         max_width = width_cut[w+1]-width_cut[w]

# for h in range(len(height_cut)-1):
#     if (height_cut[h+1]-height_cut[h]) > max_height:
#         max_height = height_cut[h+1]-height_cut[h]

# print(max_width*max_height)