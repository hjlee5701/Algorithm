import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x, cnt):
    color = graph[y][x]
    graph[y][x] = 1
    for dy, dx in direction:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == color:
            cnt = dfs(Y, X, cnt+1)
    return cnt

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
white = blue = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            white += dfs(i, j, 1)**2
        elif graph[i][j] == 'B':
            blue += dfs(i, j, 1)**2
print(white, blue)