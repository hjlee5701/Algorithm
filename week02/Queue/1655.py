import sys
import heapq
N = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
result = []

for i in range(N):

    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush( leftHeap, (-num, num))
    else:
        heapq.heappush( rightHeap, (num, num))

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min = heapq.heappop(rightHeap)[0]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush( leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))
    
    result.append(leftHeap[0][1])

for j in result: print(j)