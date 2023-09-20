import sys
from collections import deque
def bfs(start):
    result = []
    visited[start] = True
    distance[start] = 0
    queue.append(start)

    while queue:
        now = queue.popleft()          
        for city in link[now]:
            if not visited[city]:
                visited[city] = True
                queue.append(city)
                # now 도시와 연결된 도시들에 +1 하기
                distance[city] = distance[now] +1
                if distance[city] == K:
                    result.append(city)
    if len(result)==0:
        print(-1)
    else:
        result.sort()
        for i in result:
            print(i, end='\n')

N, M, K, X = map(int, sys.stdin.readline().split())
link = [ [] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)

queue = deque([])
distance = [0] * (N+1)
visited = [False] * (N+1)

bfs(X)