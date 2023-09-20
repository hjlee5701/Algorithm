import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]

dp = [10001 for _ in range(k+1)]
dp[0] = 0
for i in range(1, k+1):
    for j in coin:
        if i < j: continue
        dp[i] = min(dp[i], dp[i-j] + 1)

if dp[k] == 10001: print(-1)
else: print(dp[k])

# dp - 인덱스 : 목표 동전 금액
# dp - 값 : 최소 동전의 개수

