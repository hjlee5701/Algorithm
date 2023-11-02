from heapq import heappop, heappush
from sys import stdin
input = stdin.readline
N = int(input())
M = int(input())
way = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    way[start].append((end, cost))

start, end = map(int, input().split())
distance = [int(1e9) ]*(N+1)

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist: continue
        
        for nxtCity, nxtCost in way[now]:
            updCost = nxtCost + dist

            if updCost < distance[ nxtCity ]:
                distance[nxtCity] = updCost
                heappush(heap, (updCost, nxtCity))
dijkstra(start)
print(distance[end])

        # 비용, 최단 거리의 도시 (우선순위 : 최소비용 - 힙의 맨앞에 위치)
        # 결국 heapq에는 최소값 저장되어 필요없는 코드지만 뒤의 의미없는 연산을 막기 위함
        # 인접도시와 그에 따른 비용
            # 비용 누적
            # 선택 노드의 비용보다 누적비용이 더 작은 경우 (최단 비용 경로)