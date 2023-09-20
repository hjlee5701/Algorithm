from collections import deque
import sys
puts = sys.stdin.readline

def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def start():
    way = 1         # 초기 방향
    time = 1        # 시간
    y, x = 0, 0     # 초기 뱀 위치
    snake = deque([[y, x]])  # 방문 위치
    board[y][x] = 2          # 뱀이 지나간 곳 = 2

    while True:
        # 뱀 움직인다
        y, x = y + dy[way], x + dx[way]

        if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
            # 사과가 없는 경우
            if not board[y][x] == 1:  
                # 꼬리 제거
                tail_y, tail_x = snake.popleft()
                board[tail_y][tail_x] = 0 

            board[y][x] = 2
            snake.append([y, x])

            if time in time_info.keys():
                way = change(way, time_info[time])
            time += 1

        # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
        else:
            return time


if __name__ == "__main__":

    N = int(puts())
    K = int(puts())

    board = [[0] * N for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        board[y - 1][x - 1] = 1

    L = int(input())
    time_info = {}

    for i in range(L):
        time, turn = puts().split()
        time_info[int(time)] = turn
    print(start())