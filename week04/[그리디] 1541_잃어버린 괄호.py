# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline().strip()
n = len(input)

answer = []
index = 0
mid_sum = 0
temp = ''

for i in range(n+1):
    if i == n:
        mid_sum += int(temp)
        answer.append(mid_sum)
        break

    if 0 <= ord(input[i]) % 48 <= 9:
        temp += input[i]
    elif input[i] == '+':
        mid_sum += int(temp)
        temp = ''
    elif input[i] == '-':
        mid_sum += int(temp)
        answer.append(mid_sum)
        mid_sum = 0
        temp = ''

total = answer[0]

for i in range(1, len(answer)):
    total -= answer[i]

print(total)
