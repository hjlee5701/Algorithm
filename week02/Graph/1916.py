from heapq import heappop, heappush
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

# 출발 도시, 도착 도시, 버스 비용
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))

start, end = map(int, input().split())

# 노드간 최단 거리 정보를 업데이트/저장하는데 사용
distance = [int(1e9) ]*(N+1)

def dijkstra(start):

    # 다음 방문할 최단거리 노드를 결정하는데 사용 (우선순위 큐로 사용)
    heap = []
    heappush(heap, (0, start))

    # idx : 도착 도시 / val : 비용
    distance[start] = 0

    while heap:
        # 비용, 최단 거리의 도시 (우선순위 : 최소비용 - 힙의 맨앞에 위치)
        dist, now = heappop(heap)

        # 결국 heapq에는 최소값 저장되어 필요없는 코드지만 뒤의 의미없는 연산을 막기 위함 
        if distance[now] < dist: continue

        # 인접도시와 그에 따른 비용
        for nxtCity, nxtCost in graph[now]:

            # 비용 누적
            updCost = nxtCost + dist

            # 선택 노드의 비용보다 누적비용이 더 작은 경우 (최단 비용 경로)
            if updCost < distance[ nxtCity ]:

                distance[nxtCity] = updCost
                heappush(heap, (updCost, nxtCity))

dijkstra(start)
print(distance[end])