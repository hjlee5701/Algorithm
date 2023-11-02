import sys
input = sys.stdin.readline

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]
INF = 2**32

for gap in range(1, N):
    for start in range(0, N - gap):

        end = start + gap
        if gap == 1:
            dp[start][end] = matrix[start][0] * matrix[start][1] * matrix[end][1]
            continue

        dp[start][end] = INF

        for cur in range(start, end):
            dp[start][end] = min(dp[start][end],
                                 dp[start][cur] +
                                 dp[cur + 1][end] +
                                 matrix[start][0] * matrix[cur][1] * matrix[end][1])

print(dp[0][N - 1])