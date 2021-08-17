import sys

prime_nums=[]
a = [False, False] + [True]*(9999)
for i in range(2, 10001):
    if a[i]:
        prime_nums.append(i)
        for j in range(2*i, 10001, i):
            a[j] = False

t = int(sys.stdin.readline())

for i in range(t):
    input_num = int(sys.stdin.readline())
    check_num = input_num//2

    for j in range(input_num//2):
        if check_num in prime_nums and (input_num-check_num) in prime_nums:
            print(check_num, input_num-check_num)
            break
        check_num -= 1
    

    # ans_prime = 0
    # ans_diff = 9999

    # for prime in prime_nums:
    #     if input_num-prime in prime_nums:
    #         prime_diff = input_num-prime*2
    #         if prime_diff < ans_diff:
    #             ans_prime = prime
    #             ans_diff = prime_diff

    # print(input_num-ans_prime, ans_prime)


# 기존 방식
# all_nums = list(range(2, 5001))
# for i in range(2, 2501):
#     tmp_lst = []
#     for j in range(int(5000/i)-1):
#         tmp_lst.append(i*(j+2))
#     all_nums = list(set(all_nums).difference(set(tmp_lst)))

# 에리토스테네스







# t = int(sys.stdin.readline())

# for i in range(t):
#     input_num = int(sys.stdin.readline())
#     ans_diff = 9999
#     ans_prime = 0
#     for item in all_nums:
#         if item <= input_num/2 and (input_num-item) in all_nums:
#             item_diff = input_num-item*2
#             if item_diff < ans_diff:
#                 ans_diff = item_diff
#                 ans_prime = item 
#     print("{0} {1}".format(ans_prime, input_num-ans_prime))