import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            print('A[i], dp[i], dp[j]+1 --> ', A[i], dp[i], dp[j] + 1)
            dp[i] = max(dp[i], dp[j] + 1)
            print('A -> ', A)
            print('dp -> ', dp)
print(max(dp))