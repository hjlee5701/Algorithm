def bfs():
    dx, dy = (-1, 1, 0 , 0), ( 0, 0, -1, 1)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not 0 <= nx < C or not 0 <= ny < R:
                continue

            # 물, 고슴도치 모두 방문하지 않은 빈칸으로만 이동 가능
            if visited[ny][nx] != -1:
                continue

            # 범위 내의 방문하지 않은 좌표
            # graph[y][x] : 비버 or 물
            # graph[ny][nx] : 이동할 좌표

            # 1. 물, 고슴도치 -> 물 or 바위 
            if graph[ny][nx] == "*" or graph[ny][nx] == "X": continue

            # 2. 물 -> 비버굴
            if graph[ny][nx] == "D" and graph[y][x] == "*":  continue

            # 3. 고슴도치 -> 도착
            if graph[ny][nx] == "D" and graph[y][x] == "S":  return visited[y][x] + 1

            # 4. 물/고슴도치 -> 빈칸 (방문처리)
            queue.append((nx, ny))
            visited[ny][nx] = visited[y][x] + 1
            graph[ny][nx] = graph[y][x]
    return "KAKTUS"

from collections import deque
import sys
R, C = map(int, sys.stdin.readline().split())

# 방문처리 : (-1 = 방문X), (0 = 방문),  
visited = [[-1] * C for _ in range(R)]
queue = deque([])

graph = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]

for y in range(R):
    for x in range(C):

        if graph[y][x] == "*":
            queue.appendleft((x, y))
            visited[y][x] = 0

        elif graph[y][x] == "S":
            queue.append((x, y))
            visited[y][x] = 0

print(bfs())