import sys
s1 = [''] + list(sys.stdin.readline().strip())
s2 = [''] + list(sys.stdin.readline().strip())
len1 = len(s1)
len2 = len(s2)
dp = [['' for _ in range(len2)] for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):

        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
            else:
                    dp[i][j] = dp[i][j-1]

ans = dp[-1][-1]
print(len(ans))
if len(ans) != 0 :
    print(ans)