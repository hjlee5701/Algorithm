import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(node)


N, M = map(int, sys.stdin.readline().split())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
count = 0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1

# 연결된 노드가 없어 graph[?] 가 비었다
# 새로운 그래프로 bfs가 종료된 경우 = +1
# -> for문에 의해 새로운 탐색 실행 가능



        