def dfs(start):
    global route
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            if place[start] ==1 and place[node] == 1:
                route += 1
            elif place[node] == 0:
                dfs(node)
            elif place[node] == 1 and place[start] ==0:
                route += 1
    

import sys
sys.setrecursionlimit(2*(10**5))
N = int(sys.stdin.readline())
place = list(map(int, sys.stdin.readline().strip()))
place.insert(0, 0)

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

route = 0
for i in range(1, N+1):
    if place[i] ==1:
        visited = [False] * (N+1)
        dfs(i)
print(route)