# -*- coding: utf-8 -*-


n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
scores = [0]*11

def knapsack_recursive(scores, info, cnt, currentIndex):

    score1 = 0

    if cnt >= info[currentIndex]:
        score1 = scores[currentIndex] + knapsack_recursive(scores, info, cnt-info[currentIndex], currentIndex+1)

    score2 = knapsack_recursive(scores, info, cnt, currentIndex+1)

    return max(score1, score2)

print(knapsack_recursive(scores, info, n, 0))


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




















# # 제어문 퀴즈 #5
# from math import exp
# from random import *
# customers = 0
# for i in range(0, 50):
#     exp_time = randrange(5, 51)
#     if exp_time >= 5 and exp_time <=15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i+1, exp_time))
#         customers += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i+1, exp_time))
# print("총 탑승 승객 : {0}분".format(customers))

# # 자료구조 퀴즈 #4
# from random import *
# comments = list(range(1, 21))
# shuffle(comments)
# winners = sample(comments, 4)
# print(" -- 당첨자 발표 -- ")
# print(f"치킨 당첨자 : {winners[0]}")
# print(f"커피 당첨자 : {winners[1:]}")
# print(" -- 축하합니다 -- ")

# # 문자열 처리 퀴즈 #3
# input_url = "https://naver.com"
# my_str = input_url.replace("https://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다.".format(input_url, password))
# print(f"{input_url}의 비밀번호는 {password}입니다.")