from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [ [False] * M] * N
dp[0][0] = True
for i in range(1, M):
    if board[0][i-1] > board[0][i]:
        dp[0][i] = True
    else:
        break

for i in range(1, N):
    for j in range(1, M):
        if board[i-1][j] > board[i][j]:
            dp[i][j] = True

    for j in range(M-1):   
        if board[i][j] > board[i][j+1]:
            dp[i][j+1] = True
        
    for r in range(M-1, 0, -1):
        if board[i][r] > board[i][r-1]:
            dp[i][r-1] = True

print(dp[N-1][M-1])