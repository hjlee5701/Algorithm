from sys import stdin
import heapq
input = stdin.readline

N = int(input())
array = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

queue = []

for i in array:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
    
print(sum(queue))