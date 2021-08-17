# https://www.acmicpc.net/problem/4344

import sys

t = int(sys.stdin.readline())

for i in range(t):
    tmp_lst = list(map(int,sys.stdin.readline().split()))
    num_student = tmp_lst[0]
    tmp_lst.pop(0)
    
    total_score = 0
    for score in tmp_lst:
        total_score += score
    
    avg_score = total_score/num_student

    good_student = 0
    for score in tmp_lst:
        if score > avg_score:
            good_student += 1
    
    print("{:.3f}%".format(round((good_student/num_student)*100, 3)))
