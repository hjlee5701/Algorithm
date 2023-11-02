from sys import stdin
sTxt = list(stdin.readline().strip())

N = len(sTxt)
table = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    table[i][i] = True

for i in range(N-1):
    if sTxt[i] == sTxt[i+1]:
        table[i][i+1] = True

for i in range(N-2):
    for j in range(N-2-i):
        j = i + j + 2
        if sTxt[i] == sTxt[j] and table[i + 1][j - 1]:
            table[i][j] = True 

dp = [1] + [0 for _ in range(N)]
for i in range(1, N):
    minVal = dp[i - 1] + 1
    for j in range(i):
        if table[j][i]:
            minVal = min(minVal, dp[j-1] +1)
    dp[i] = minVal
print(dp[-1])


# for question in range(M):
#     s, e = map(int, input().split())
#     print(table[s-1][e-1])


# BBCDDECAECBDABADDCEBACCCBDCAABDBADD
# BB C DD (ECAECB) DABAD D (CEBA) CCC (BDCA) ABDBA DD

# 팰린드롬 나누기
