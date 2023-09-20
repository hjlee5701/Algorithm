def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1
    seaList = []

    while queue:
        y, x = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if not graph[ny][nx]:
                    sea += 1
                elif graph[ny][nx] and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = 1
        if sea > 0:
            seaList.append((y, x, sea))
    for y, x, sea in seaList:
        graph[y][x] = max(0, graph[y][x] - sea)

    return 1

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

# graph : 입력값
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# ice : 빙산의 좌표
ice = []
for y in range(N):
    for x in range(M):
        if graph[y][x]:
            ice.append((y,x))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0
# 빙산 1개
while ice:
    visited = [[0] * M for _ in range(N)]
    delList = []        # 없어진 빙산의 좌표/바다
    group = 0           # 빙산의 개수

    for y, x in ice:
        if graph[y][x] and not visited[y][x]:
            group += bfs(y, x)

        if graph[y][x] == 0:
            delList.append((y, x))

    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)
