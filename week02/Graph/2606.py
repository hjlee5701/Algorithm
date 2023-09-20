import sys
def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

visited = [False] * (N+1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(sum(visited)-1)