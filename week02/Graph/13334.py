import sys
import heapq
n = int(sys.stdin.readline())

road_info = []
for _ in range(n):
    home, office = map(int, sys.stdin.readline().split())
    road_info.append([home, office])

d = int(sys.stdin.readline())

roads = []
for way in road_info:
    home, office = way
    if abs(home - office) <= d:
        way.sort()
        roads.append(way)

roads.sort(key=lambda x: (x[1]))

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while d < road[1] - heap[0][0]:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)
        








# arr = []
# for _ in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     if a > b:
#         arr.append((b, a))
#         continue
#     arr.append((a, b))

# d = int(sys.stdin.readline())
# way = []
# for a in arr:
#     if a[1]-a[0] < d:
#         way.append((a[0], a[1]))

# way.sort(key=lambda x: (x[1], x[0]))


