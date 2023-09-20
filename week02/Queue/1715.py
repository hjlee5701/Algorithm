import heapq
import sys

N = int(sys.stdin.readline())
cards = []
result = 0

for _ in range(N):
    inputCard = int(sys.stdin.readline())
    heapq.heappush(cards, inputCard)

if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        heapq.heappush(cards, a+b)
        result += a+b
    print(result)