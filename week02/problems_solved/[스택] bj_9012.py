# https://www.acmicpc.net/problem/9012

import sys

t = int(sys.stdin.readline())
data = []
for i in range(0, t):
    data.append(sys.stdin.readline().strip())

for j in range(0, t):

    chk_stack = 0
    boolean = True

    if data[j][0] == ")":
        boolean = False
    else:
        for k in range(0, len(data[j])):
            if data[j][k] == "(":
                chk_stack += 1
            elif data[j][k] == ")":
                chk_stack -= 1

            if chk_stack < 0:
                boolean = False
                break

    if boolean == False:
        print("NO")
    else:
        if chk_stack == 0:
            print("YES")
        else:
            print("NO")