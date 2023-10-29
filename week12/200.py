class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        col, row = len(grid), len(grid[0])
        for i in range(col):
            for j in range(row):
                # 1을 찾았다면 초기 시작점을 queue 에 넣기 (초기값 설정)
                if grid[i][j] == '1':
                    queue = collections.deque([(i, j)])
                    # 중복 탐색 방지
                    grid[i][j] = '2'

                    while queue:
                        # 시작점에서 상하좌우 탐색
                        c, r = queue.popleft()
                        for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
                            dx, dy = c+x, r+y
                            if 0 <= dx < col and 0 <= dy < row and grid[dx][dy] == '1':
                                # 시작지점 근처에 1이 있다면 다음 탐색을 위한 시작지점으로 설정
                                queue.append((dx, dy))

                                # 중복 탐색 방지
                                grid[dx][dy] = '2'
                    res += 1
        return res