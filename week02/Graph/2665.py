def bfs():
    queue = deque([])
    queue.append((0, 0))
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    # 흰색방
                    if board[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx, ny))
                    # 검정색 방
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

import sys
from collections import deque
N = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().strip())))
visited = [[-1] * N for _ in range(N)]
print('check', board[0][2])

bfs()
print(visited[N-1][N-1])