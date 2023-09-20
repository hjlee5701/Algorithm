import sys
from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=' ')
    
    for node in graph[start]:
        if not visited[node]:
            dfs( node )

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()

# DFS
visited = [False] * (N+1)
dfs(V)
print()

# BFS
visited = [False] * (N+1)
bfs(V)
print()