import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
queue = deque([])
result = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    degree[B] +=1

for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    idx = queue.popleft()
    result.append(idx)
    for i in graph[idx]:
        degree[i] -=1
        if degree[i] == 0:
            queue.append(i)
print(*result)
