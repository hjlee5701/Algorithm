import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    # dp[n] : n원에 대한 동전 교환 방법 개수
    dp = [0] * (M+1)

    # 동전 정보
    coin_info = []

    # 아무도 동전을 사용하지 않는 경우
    dp[0] = 1
    for coin in coins:
    # 총 T원부터 1원까지 진행
        for money in range(M, 0, -1):

            # 현재 coin 동전 개수만큼 반복문
            for i in range(1, (M//coin) +1):

                if money - coin * i >= 0:
                    
                    dp[money] += dp[money - coin * i]
    print('result ->',dp[M])