from sys import stdin
input = stdin.readline

# 물품 수, 무게
N, K = map(int, input().split())
bag = [(0,0)] + [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    wgt, val = bag[i][0], bag[i][1]

    for j in range(1, K+1):
        if j < wgt:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],
                           dp[i-1][j-wgt] + val)
print(dp[-1][-1])