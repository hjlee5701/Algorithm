def dfs(start, group):
    global isError
    
    if isError: return

    visited[start] = group

    for node in graph[start]:
        if not visited[node]:
            dfs(node, -group)

        elif visited[node] == visited[start]:
            isError = True
            return

import sys
sys.setrecursionlimit(20000)
T = int(sys.stdin.readline())

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)

    isError = False
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i, 1)
    if isError:
        print('NO')
    else:
        print('YES')