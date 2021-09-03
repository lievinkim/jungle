import sys

n = int(sys.stdin.readline().strip())

data = [0]
for i in range(n):
    data.append(int(sys.stdin.readline().strip()))

dp = [0]
dp.append(data[1])

if n > 1:
    dp.append(data[1] + data[2])

for i in range(3, n + 1):
    dp.append(max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i]))

print(dp[n])