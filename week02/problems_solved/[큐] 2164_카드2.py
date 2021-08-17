# https://www.acmicpc.net/problem/2164

import sys
t = int(sys.stdin.readline())

data = [i for i in range(1, t+1)]

front_index = 0
cnt = len(data)

while cnt > 1:

    # 첫 번째 카드 버리기
    front_index += 1
    cnt -= 1

    # 두 번째 카드 뒤로 보내기
    data.append(data[front_index])
    front_index += 1

print(data[front_index])