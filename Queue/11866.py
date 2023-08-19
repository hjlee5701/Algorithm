import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

queue = deque([ n for n in range(1, N+1)])
result = []
for _ in range(N):
    queue.rotate(-K+1)
    result.append(str(queue.popleft()))

print("<"+", ".join(result)+">")