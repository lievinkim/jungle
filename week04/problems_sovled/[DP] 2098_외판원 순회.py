# https://www.acmicpc.net/problem/2098

import sys
n = int(sys.stdin.readline())
w = []
for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))
dp = [[-1] * (1<<n) for _ in range(n)]

INF = float('inf')

def solution(x, visited):

    if visited == (1<<(n-1))-1: # n=4일 때, 111은 모든 도시를 방문한 경우를 의미
        if w[x][0]: # 마지막 도시에서 0으로 돌아가는 경로가 있다면 해당 비용 리턴
            return w[x][0]
        else: # 없다면 없다는 의미로 INF 리턴
            return INF

    if dp[x][visited] != -1: # 방문한 적이 있다면
        return dp[x][visited]

    dp[x][visited] = INF

    for i in range(1, n):
        if not w[x][i]:
            continue
        if visited & (1<<(i-1)):
            continue
        next = solution(i, visited | (1<<(i-1))) + w[x][i]
        dp[x][visited] = min(dp[x][visited], next)
    return dp[x][visited]

print(solution(0, 0))