# https://www.acmicpc.net/problem/2294

import sys
from collections import deque

# 데이터 입력 받기
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    x = int(sys.stdin.readline())
    coins.append(x)
coins = list(set(coins))
num_of_coins = len(coins)

data = []
for i in range(0, num_of_coins):
    for j in range(i, num_of_coins):
        if coins[i] == coins[j]:
            data.append([coins[i], 1])
        elif (coins[i]+coins[j]) not in coins:
            data.append([coins[i]+coins[j], 2])

data.sort(key = lambda x: x[0])

ans = None

for _ in range(len(data)):
    queue = deque()
    left = k
    cnt = 0

    for item in data:
        queue.append(item)

    while queue:
        check_num = queue.pop()
        print(check_num)
        print(ans)
        cnt += left // check_num[1]
        left = left % check_num[0]

        if left == 0:
            if ans == None:
                ans = cnt
            else:
                ans = min(ans, cnt)
            queue.clear()

if ans == None:
    print(-1)
else:
    print(ans)

