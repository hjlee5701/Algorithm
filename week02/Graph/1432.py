def topology_sort():
    heap = []
    for i in range(1, N+1):
        if degree[i] == 0:
            heapq.heappush(heap, -i)
    n = N
    while heap:
        now = -heapq.heappop(heap)
        answer[now] = n

        for i in graph[now]:
            degree[i] -= 1
            if degree[i] == 0:
                heapq.heappush(heap, -i)
        n -= 1

import sys
import heapq
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for i in range(1, N+1):
    tmp = [0] + list(map(int, sys.stdin.readline().strip()))
    for j in range(1, N+1):
        if tmp[j] == 1:
            graph[j].append(i)
            degree[i] += 1

answer = [0] * (N+1)

topology_sort()
if answer.count(0) > 1:
    print(-1)
else:
    print(*answer[1:])