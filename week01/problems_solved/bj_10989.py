import sys

t = int(sys.stdin.readline())
data = [0]*10001

for i in range(0, t):
    num = int(sys.stdin.readline())
    data[num] = data[num] + 1

for j in range(1, len(data)):
    for k in range(data[j]):
        print(j)
