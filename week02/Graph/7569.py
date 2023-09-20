def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H :
                tomato = graph[nz][ny][nx]
                if tomato == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append([nx, ny, nz])
    day = 0
    for z in graph:
        for y in z:
            for x in y:
                if x==0:
                    print(-1)
                    exit(0)
            day = max(day,max(y))
    print(day-1)

import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

# 좌우앞뒤위아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

graph = []
queue = deque([])
for z in range(H):
    tomato = []
    for y in range(N):
        tomato.append(list(map(int, sys.stdin.readline().split())))
        for x in range(M):
            if tomato[y][x] == 1:
                queue.append([x, y, z])
    graph.append(tomato)
bfs()