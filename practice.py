# -*- coding: utf-8 -*-

import sys
n, m = map(int, sys.stdin.readline().split())

edges = []
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edges.append([a, b])

edges.sort(lambda x: (x))

print(edges)


# dp = []
# max_sum = 0
# temp = 0

# for i in range(n):
#     if input_lst[i] > 0:
#         temp += input_lst[i]
#         print(temp)
#     else:
#         max_sum = max(max_sum, temp)
#         temp = 0

# if max_sum == 0:
#     temp = input_lst[0]
#     for j in range(1, n):
#         if input_lst[j] > temp:
#             temp = input_lst[j]
#     max_sum = temp

# print(max_sum)


# apeach_score = 0
# apeach_cnt = n
# for i in range(len(info)):
#     if apeach_cnt > 0:
#         apeach_score += 10-i
#         apeach_cnt = apeach_cnt-info[i]
#     else:
#         break

# ryan_info = [0]*11
# ryan_score = 0
# answer = []
# cnt = n

# for i in range(0, 10):
#     for j in range(i+1, 10):


#     info_index = i

#     while cnt > 0:
#         if (cnt > info[info_index]):
#             ryan_info[info_index] = info[info_index]+1
#             cnt = cnt - (info[info_index]+1)
#             info_index+=1
#             if info_index == 10:
#                 ryan_info[info_index] = cnt
#                 break
#         else:
#             info_index+=1
#             if info_index == 10:
#                 ryan_info[info_index] = cnt
#                 break
    
#     temp_score = 0
#     temp_cnt = n
#     for i in range(len(ryan_info)):
#         if ryan_info[i] != 0:
#             temp_score += 10-i
    
#     if temp_score > ryan_score:
#         answer = ryan_info
#         ryan_score = max(ryan_score, temp_score)

#     cnt = n
#     ryan_info = [0]*11

# apeach_score = 0
# apeach_cnt = n
# for i in range(len(info)):
#     if info[i] != 0 and answer[i]==0:
#         apeach_score += 10-i

# if apeach_score > ryan_score:
#     answer = [-1]

# print(answer)









# print(list_converted)

# temp = ''
# for i in range(len(converted)):
#     if converted[i] != '0':
#         temp = temp + converted[i]
#         continue
#     elif converted[i] == '0' and temp != '':
#         list_converted.append(temp)
#         temp = ''
#     else:
#         continue

# if temp != '':
#     list_converted.append(temp)

# for number in list_converted:
#     if is_prime(int(number)):
#         answer += 1

# print(answer)




















# # ????????? ?????? #5
# from math import exp
# from random import *
# customers = 0
# for i in range(0, 50):
#     exp_time = randrange(5, 51)
#     if exp_time >= 5 and exp_time <=15:
#         print("[O] {0}?????? ?????? (???????????? : {1}???)".format(i+1, exp_time))
#         customers += 1
#     else:
#         print("[ ] {0}?????? ?????? (???????????? : {1}???)".format(i+1, exp_time))
# print("??? ?????? ?????? : {0}???".format(customers))

# # ???????????? ?????? #4
# from random import *
# comments = list(range(1, 21))
# shuffle(comments)
# winners = sample(comments, 4)
# print(" -- ????????? ?????? -- ")
# print(f"?????? ????????? : {winners[0]}")
# print(f"?????? ????????? : {winners[1:]}")
# print(" -- ??????????????? -- ")

# # ????????? ?????? ?????? #3
# input_url = "https://naver.com"
# my_str = input_url.replace("https://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}??? ??????????????? {1}?????????.".format(input_url, password))
# print(f"{input_url}??? ??????????????? {password}?????????.")