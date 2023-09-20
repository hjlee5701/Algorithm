import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def dfs(start):
    for node in graph[start]:
        if visited[node] == 0:
            visited[node] = start
            dfs(node)   
dfs(1)

for x in range(2, N+1):
    print(visited[x])