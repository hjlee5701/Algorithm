from heapq import heappush, heappop
from sys import stdin

N = int(stdin.readline())
heap = []
result = 0

for _ in range(N):
    heappush(heap, int(stdin.readline()))

if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, a+b)
        result += a+b
    print(result)