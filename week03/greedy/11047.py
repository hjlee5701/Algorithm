import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

cnt = 0
for n in range(N):
    cnt += K//coins[n]
    K = K % coins[n]

print(cnt)