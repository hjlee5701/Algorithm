import sys
T = int(sys.stdin.readline())
k = int(sys.stdin.readline())

# dp[n] : n원에 대한 동전 교환 방법 개수
dp = [0] * (T+1)

# 동전 정보
coin_info = []

# 아무도 동전을 사용하지 않는 경우
dp[0] = 1

for _ in range(k):
    coin, num = map(int, sys.stdin.readline().split())
    coin_info.append((coin, num))

# 입력 받은 동전 꺼내기
for coin, num in coin_info:

    # 1원 ~ 목표금액까지의 테이블 생성을 위한 반복문
    for index in range(T, 0, -1):

        # 1개 ~ 입력받은 동전의 개수
        for i in range(1, num+1):

            # 테이블 컬럼 - 입력받은 동전 * 개수
            if index - coin * i >= 0:
              
                dp[index] += dp[index - coin * i]
print(dp[T])