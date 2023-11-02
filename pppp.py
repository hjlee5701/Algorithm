import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

maximum = 100001
visited = [0] * maximum
queue = deque([N])
while queue:
    now = queue.popleft()
    if now == K:
        print(visited[now])
        break
    
    for next in (now-1, now+1, now *2):
        if 0 <= next < maximum and not visited[next]:
            visited[next] = visited[now]+1
            queue.append(next)