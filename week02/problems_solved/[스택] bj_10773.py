# https://www.acmicpc.net/problem/10773

import sys
t = int(sys.stdin.readline())
data = []

for i in range(0, t):
    num = int(sys.stdin.readline())

    if num == 0:
        data.pop(len(data)-1)
        continue
    
    data.append(num)

ans = 0
for item in data:
    ans += item

print(ans)
