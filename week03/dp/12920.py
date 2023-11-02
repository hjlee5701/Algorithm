from sys import stdin
input = stdin.readline

# 물건 종류 / 가방 최대 무게
N, M = map(int, input().split())

dp = [0 for _ in range(M+1)]
weight, satisLvl = [], []

for _ in range(N):
    # 물건 무게 / 만족도 / 물건 개수
    V, C, K = map(int, input().split())

    idx = 1
    while K > 0:
        tmp = min(idx, K)

        weight.append(V * tmp)
        satisLvl.append(C * tmp)
        idx *= 2
        K -= tmp

for i in range(len(weight)):
    for j in range(M, 0, -1):
        if j >= weight[i]:
            dp[j] = max(dp[j], dp[j-weight[i]] + satisLvl[i])

print(dp[M])