# https://www.acmicpc.net/problem/11866

import sys
a, b = map(int, sys.stdin.readline().split())
data = [i for i in range(1, a+1)]

start_index = b-1
interval_num = b-1
cnt = len(data)

ans = []

while cnt > 0:
    ans.append(data[start_index])
    del data[start_index]
    cnt -= 1

    if cnt == 0:
        break

    start_index += interval_num

    if start_index >= cnt:
        start_index = start_index % cnt

print("<", end="")
for i in range(0, len(ans)-1):
    print("{0}, ".format(ans[i]), end="")
print("{0}".format(ans[len(ans)-1]), end="")
print(">")