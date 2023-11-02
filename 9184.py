def dfs(num):
    if num <= 0:
        return 1

    for i in range(20):
        dp[i] = dp[i]
        pass

from sys import stdin
input = stdin.readline
a, b, c = map(int, input().split())

dp = [1] + [0] * 20
while True:
    a, b, c = map(int, input().split())
    dfs(min(a, b, c))

    if a==-1 and b==-1 and c==-1:
        break