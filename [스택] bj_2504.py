# https://www.acmicpc.net/problem/2504

import sys
data = list(map(str, sys.stdin.readline().strip()))
n = len(data)

if data[n-1] in ["(", "["]:
    print(0)

chk = [0, 0]
false_chk = True
closed_chk = False
group_chk = False
scores = []
stacks = []
for i in range(n-1, -1, -1):
    if data[i] == ")":
        chk[0] += 1
        if closed_chk == True:
            group_chk = True
        closed_chk = False
    elif data[i] == "(":
        chk[0] -= 1
        if chk[0] < 0:
            false_chk = False
            break
        else:
            if temp == 0:
                stacks.append(2)
            elif group_chk == True:
                temp += 2
                group_chk = False 
            else:
                temp = temp*2
        closed_chk = True

        if chk[0] == 0 and chk[1] == 0:
                scores.append(temp)
                closed_chk = False
                temp = 0    
        
    elif data[i] == "]":
        chk[1] += 1
        if closed_chk == True:
            group_chk = True
        closed_chk = False
    elif data[i] == "[":
        chk[1] -= 1
        if chk[1] < 0:
            false_chk = False
            break
        else:
            if temp == 0:
                temp += 3
            elif group_chk == True:
                temp += 2
                group_chk = False 
            else:
                temp = temp*3
        closed_chk = True
        if chk[0] == 0 and chk[1] == 0:
            scores.append(temp)
            temp = 0

if false_chk == False:
    print(0)
else:
    ans = 0
    for score in scores:
        ans += score
    print(ans)