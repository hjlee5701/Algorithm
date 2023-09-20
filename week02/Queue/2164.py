import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([ n for n in range(1, N+1)])

for _ in range(N-1):
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])