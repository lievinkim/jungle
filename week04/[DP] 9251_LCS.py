# https://www.acmicpc.net/problem/9251

import sys

input_arr = []
for _ in range(2):
    temp = sys.stdin.readline().strip()
    temp_lst = []
    for i in range(len(temp)):
        temp_lst.append(temp[i])
    input_arr.append(temp_lst)

main_length = len(input_arr[0])
compare_length = len(input_arr[1])
first_letter_dp_table = [0]*57

answer = []

for i in range(compare_length):

    for item in answer:
        for j in range(item[2]+1, i+1):
            if input_arr[0][j] == input_arr[1][i]:
                item[0] = item[0] + input_arr[1][i]
                item[1] += 1
                item[2] = j

    temp = ord(input_arr[1][i]) % 65

    if first_letter_dp_table[temp] != 0:
        continue
    
    for j in range(0, i+1):
        if input_arr[0][j] == input_arr[1][i]:
            answer.append([input_arr[0][j], 1, j])
            first_letter_dp_table[temp] = 1

answer.sort(key=lambda x: (-x[1]))
print(answer[0][1])