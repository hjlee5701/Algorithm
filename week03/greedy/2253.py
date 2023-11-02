from sys import stdin
from math import sqrt
input = stdin.readline

def solve():
    N, M = map(int, input().split())
    dp = [[float('inf')] * (int(sqrt(2*N))+2) for _ in range(N+1)]
    dp[1][0] = 0
    trap = set()
    for _ in range(M):
        trap.add(int(input()))
    
    for i in range(2, N+1):
        if i in trap:
            continue
        for v in range(1, int(sqrt(2*i)) + 1): # v 범위를 제한 => 들어오는 i에 대해서만
            dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1
    
    result = min(dp[N])
    if result == float('inf'):
        print(-1)
    else:
        print(result)

solve()
# https://woonys.tistory.com/entry/%EC%A0%95%EA%B8%80%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90-29%EC%9D%BC%EC%B0%A8-TIL-%EC%A0%90%ED%94%842253-%EB%A9%80%ED%8B%B0%ED%83%AD-%EC%8A%A4%EC%BC%80%EC%A5%B4%EB%A7%811700