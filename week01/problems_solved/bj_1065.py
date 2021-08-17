# https://www.acmicpc.net/problem/1065

import sys

t = int(sys.stdin.readline())
count = 0

for num in range(1, t+1):
    
    digits = []
    digit_num = len(str(num))

    for i in range(digit_num):
        digits.append(i) # 세 자릿수라면 [0, 1, 2]

    for j in range(len(digits)):
        digits[(len(digits)-1)-j] = (num//(10**j))%10

    
    if len(digits) <= 2:
        count+=1
    else:
        num_diff = digits[1]-digits[0]

        for k in range(1, len(digits)-1):
            bool_num = True
            if (digits[k+1]-digits[k] != num_diff):
                bool_num = False
                break
            if bool_num:
                count+=1

print(count)

        
    


# if t < 100:
#     count = t
# elif 100 <= t < 1000:
#     count = 99
#     for num in range(100, t+1):
#         t1 = (num//1)%10
#         t2 = (num//10)%10
#         t3 = (num//100)%10
#         if (t1 < t2 < t3) and (t3-t2)==(t2-t1):
#             count += 1
#         if (t1 > t2 > t3) and (t1-t2)==(t2-t3):
#             count += 1
# elif t == 1000:
#     count = 99
#     for num in range(100, t+1):
#         t1 = (num//1)%10
#         t2 = (num//10)%10
#         t3 = (num//100)%10
#         if (t1 < t2 < t3) and (t3-t2)==(t2-t1):
#             count += 1
#         if (t1 > t2 > t3) and (t1-t2)==(t2-t3):
#             count += 1
