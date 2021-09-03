# https://www.acmicpc.net/problem/2253

import sys

# by DP
# 변수 N : 전체 돌 개수
# 변수 M : 작은 돌 개수
N, M = map(int, sys.stdin.readline().split())

# 변수 INF : 무한 값을 표현하는 변수
INF = float('inf')

# 변수 approx : 속도가 계속 1씩 증가하며 N에 도달한다고 했을 때 속도 근사값
# 해당 값은 최대 속도값으로 답은 해당 속도값보다 높을 수 없다.
# 따라서 불필요하게 더 높은 값은 체크하지 않도록 하기 위해 근사값을 구한다.
# (int((2*N)**0.5)+1)이나 0 인덱스는 포함하지 않기 때문에 +2를 했다.
approx = (int((2*N)**0.5)+2)

# 변수 dp : 현재 위치(행)와 현재 속도(열)에 대한 점프 횟수를 기록해 놓은 테이블
# 현재 아무 것도 파악된 것이 없기 때문에 INF로 초기화 해놓았으며,
# dp[1][0]은 현재 위치 1에서 속도는 0이라는 가장 기본값에 해당함으로 추가한다.
dp = [[INF] * approx for _ in range(N+1)]
dp[1][0] = 0

# 변수 small_rock : 작은 돌의 번호를 모아 놓은 셋 정렬
# 변수 small_rock에 input 값 받기
small_rock = set()
for _ in range(M):
    small = int(sys.stdin.readline())
    small_rock.add(small)

# 1를 제외한 2부터 N까지를 대입하는 것으로 전체 돌에 대하여 체크하기 위함
for i in range(2, N+1):

    # 만약 특정 돌이 작은 돌에 해당하는 경우에는 넘어감
    if i in small_rock:
        continue
    
    # dp[1][0]은 구해졌으니 dp[2][j]의 최소값을 구하기 위한 공식이다
    # 마찬가지로 j의 최대 속도는 돌의 수에 영향을 받기 때문에 range를 새롭게 설정한다
    for j in range(1, int((2*i)**0.5)+1):

        # d[i][j]는 결국 i라는 위치에 j라는 속도를 가지고 도달 했을 때의 최소 점프 횟수이다.
        # 이는 그 직전 경우의 수에서 1을 더한 것이며, 직전 경우의 수는 3가지로 구분할 수 있다.
            # dp[i-j][j-1]
            # dp[i-j][j]
            # dp[i-j][j+1]
        # i-j : 이미 j라는 속도를 가지고 i에 도달했기 때문에 i-j는 직전 위치가 된다.
        # 이때 i-j라는 위치에서의 속도는 j-1, j, j+1로 나눌 수 있다.
        # j-1이라면 j-1에서 속도가 1 증가하여 현재 i 위치에 j 속도를 가지게 되었다고 볼 수 있다.
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1])+1

if min(dp[N]) == INF:
    # 최종적으로 dp[N][x]에 저장된 여러 최소값이 INF라며 도달하지 못한 경우로 -1를 리턴한다.
    print(-1)
else:
    # 최종적으로 dp[N][x]들 중에서 가장 작은 숫자가 기록된 경우가 점프 횟수 최소값일 때이다. 
    print(min(dp[N]))