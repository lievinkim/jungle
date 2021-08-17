# https://www.acmicpc.net/problem/2503

import sys

t = int(sys.stdin.readline())
data = []
for _ in range(0, t):
    data.append(list(map(int, sys.stdin.readline().split())))

def baseball_chk(n, c:int, s, b):

    str_c = str(c)
    strike = 0
    ball = 0

    for i in range(0, len(n)):
        for j in range(0, len(str_c)):
            if n[i] == str_c[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    
    if strike == s and ball == b:
        return True
    else:
        return False

candidate = []

for num in range(100, 1000):

    str_num = str(num)
    bool_ans = True

    if int(str_num[0]) == 0 or int(str_num[1]) == 0 or int(str_num[2]) == 0:
        continue

    if str_num[0] == str_num[1] or str_num[0] == str_num[2] or str_num[1] == str_num[2]:
        continue

    for i in range(0, len(data)):
        test = baseball_chk(str_num, data[i][0], data[i][1], data[i][2])
        if test == False:
            bool_ans = False
            break
        
    if bool_ans == True:
        candidate.append(num)

print(len(candidate))