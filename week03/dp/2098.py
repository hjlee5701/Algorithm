import sys
N = int(sys.stdin.readline())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (1 << N) for _ in range(N)]
VISIT_CLEAR = (1 << N) - 1
INF = float('inf')

def dfs(now, visited):

    # N개의 도시 모두 방문 여부 확인
    if visited == VISIT_CLEAR:
        if cities[now][0]:
            return cities[now][0] or INF
    
    # 이전에 계산된 경우 결과 반환 (now까지 방문한 최소비용)
    if dp[now][visited] != 0:
        return dp[now][visited]
    
    tmp = INF
    for nxt in range(N):
        if visited & (1 << nxt) == 0 and cities[now][nxt] != 0:
            tmp = min(tmp, dfs(nxt, visited | (1 << nxt)) + cities[now][nxt])
    dp[now][visited] = tmp
    return tmp

print(dfs(0, 1 << 0))