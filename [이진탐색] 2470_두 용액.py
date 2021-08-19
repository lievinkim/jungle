# https://www.acmicpc.net/problem/2470

import sys

t = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

answer = []

for _ in range(t-1):
    standard = data[0]
    del data[0]

    start_index = 1
    end_index = len(data)-1

    while start_index <= end_index:
        mid_index = (start_index+end_index)//2
        mid_value = data[mid_index]
        new_value = standard + data[mid_index]


        if diff == None:
            diff = new_value
        elif new_value >= diff:
            start_index = mid_index+1
        elif abs(new_value) < diff:
            end_index = mid_index-1

        if len(answer) == 0:
            answer.append(standard)
            answer.append(data[mid_index])
            answer.append(abs(new_value))
        elif abs(new_value) < answer[2]:
            answer.clear()
            answer.append(standard)
            answer.append(data[mid_index])
            answer.append(abs(new_value))

print(answer[0], answer[1])

        

