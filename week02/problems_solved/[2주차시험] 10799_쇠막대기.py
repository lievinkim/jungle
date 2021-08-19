# https://www.acmicpc.net/problem/10799

import sys
input_value = sys.stdin.readline().strip()
data = []
for i in range(len(input_value)):
    data.append(input_value[i])

stick = 0
is_previous = None
cutted = 0

for i in range(len(data)):
        
    if data[i] == '(':
        stick += 1
        is_previous = data[i]
    elif data[i] == ')':
        if is_previous == '(':
            stick -= 1
            cuts = stick
            cutted += cuts
        elif is_previous == ')':
            stick -= 1
            cuts = 1
            cutted += cuts
        is_previous = data[i]

print(cutted)