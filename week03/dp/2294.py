import sys
n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

dp = [10001 for _ in range(k+1)]
dp[0] = 0

for idx in range(1, k+1):
    for coin in coins:
        if idx < coin: continue
        dp[idx] = min(dp[idx], dp[idx-coin] + 1)

if dp[k] == 10001: print(-1)
else: print(dp[k])
