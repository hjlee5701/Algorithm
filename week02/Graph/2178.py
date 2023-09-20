import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

# 각각 x축과 y축 방향으로 이동할 때의 변화량 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# maze = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [...] ] 
maze = []
for i in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

queue = deque([])
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # (N, M) = 미로의 끝에 도달하기
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

print(maze[N-1][M-1])
