def tsp(D):
    N = len(D)
    inf = float('inf')
    ans = inf # 정답을 '무한'으로 초기화한다.
    VISITED_ALL = (1 << N) - 1

    def find_path(start, last, visited, tmp_dist):
        
        nonlocal ans
        
        if visited == VISITED_ALL:
            return_home_dist = D[last][start] or inf
            ans = min(ans, tmp_dist + return_home_dist)
            return

        for city in range(N):
            if visited & (1 << city) == 0 and D[last][city] != 0:
                find_path(start, city, visited | (1 << city), tmp_dist + D[last][city])
        
    for c in range(N):
        find_path(c, c, 1 << c, 0)

    return ans




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