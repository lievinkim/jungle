


import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adjacent_lst = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjacent_lst[a].append(b)
    adjacent_lst[b].append(a)

def dfs_iteration(graph, start):

    visited = []
    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    
    print(len(visited)-1)

def dfs_recursion(graph, start, visited=[]):

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursion(graph, node, visited)

    return len(visited)-1

# dfs_iteration(adjacent_lst, 1)
print(dfs_recursion(adjacent_lst, 1))























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