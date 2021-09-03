# https://www.acmicpc.net/problem/2253

import sys
from collections import deque

# by BFS
# 변수 N : 전체 돌 개수
# 변수 M : 작은 돌 개수
N, M = map(int, sys.stdin.readline().split())

# 변수 check : 전체 돌 체크 여부 (N개 혹은 계산 편의를 위해 N+1개)
# 이 때 정렬 안에 또 다른 정렬을 생성한 이유는 동일한 위치에 대하여 어떤 점프를 통해 들어왔는 지를 구분하기 위함
# 예를 들어 1만큼 점프해서 A라는 돌에 도착한 것과 2만큼 점프해서 A라는 돌에 도착한 것을 구분하기 위함 (check[A] = [1, 2])
check = [[] for _ in range(N+1)]

# 변수 small_rock : 작은 돌의 번호를 모아 놓은 셋 정렬    
small_rock = set()

# 변수 small_rock에 input 값 받기
for _ in range(M):
    small = int(sys.stdin.readline())
    small_rock.add(small)

# 매개변수 N : 현재 위치
# 매개변수 check : 전체 돌 체크 여부를 표시하는 정렬
# 매개변수 small_rock : 작은 돌 셋 정렬
def solution(N, check, small_rock):

    # 큐에 저장하는 값은
    # 현재 위치, 이전 점프, 점프 횟수 (따라서 초기값은 1, 0, 0으로 입력)
    queue = deque([(1, 0, 0)])
    while queue:
        location, jump, n = queue.popleft()

        # 점프가 가능한 경우의 수 3가지
        # 점프 유지, 점프 +1 증가, 점프 -1 감소
        for x in [jump, jump+1, jump-1]:

            # x가 0 초과일 때만 진행 (0인 경우에는 현재 위치 변동 X)
            if x > 0:

                # 변수 next_location : 현재 위치에서 점프한 만큼 더한 값
                # 최대 3가지 next_location 발생 : current + jump / current + (jump+1) / current + (jump-1)
                next_location = location + x

                # next_location이 마지막 돌에 도착했을 때
                # 점프 횟수에 1을 더한 다음에 해당 결과값 리턴
                if next_location == N:
                    return n + 1

                # 다음 3가지 조건인 경우 
                # 첫째, next_location이 전체 돌 개수인 N 이하
                # 둘째, next_location이 작은 돌 셋에 미포함
                # 셋째, next_location의 체크 내 정렬에 미포함
                if next_location < N and next_location not in small_rock and x not in check[next_location]:
                    # check 정렬에 점프 수치를 기록
                    # 점프하고 난 후의 위치, 점프, 횟수를 queue에 저장
                    check[next_location].append(x)
                    queue.append((next_location, x, n+1))

    # 모든 작업이 끝났음에도 N에 도달하지 못한 경우 -1을 리턴
    return -1

print(solution(N, check, small_rock))