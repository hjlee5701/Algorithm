import sys
s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

len1, len2 = len(s1), len(s2)

# 인덱스 0은 비교에서 제외 (아래의 i-1, j-1 의 마진값 설정) 
dp = [[0] * (len1+1) for _ in range(len2+1)]

for i in range(1, len2+1):
    for j in range(1, len1+1):

        # 0이 아닌 1부터 비교시작하므로 인덱스를 맞추기 위해 -1 하기
        if s1[j-1] == s2[i-1]:

            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len2][len1])