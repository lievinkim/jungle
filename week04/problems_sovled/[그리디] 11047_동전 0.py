# https://www.acmicpc.net/problem/11047

import sys
N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

cnt = 0

while K > 0 and N > 0:
    temp = K//coins[N-1]
    cnt += temp
    
    K = K % coins[N-1]
    N -= 1

print(cnt)