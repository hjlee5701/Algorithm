import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

needs = [[0] * (N+1) for _ in range(N+1)]   # 각 제품을 만드는데 필요한 부품, 필요 개수
link = [[] for _ in range(N+1)]             # 연결 정보
degree = [0] * (N+1)                        # 진입 차수
queue = deque([])
                                            # Y --- (K개) -- > X
for _ in range(M):                          # 기본/중간부품 `Y`는 `X`를 만드는데 `K`개가 필요 
    X, Y, K = map(int, sys.stdin.readline().split())
    link[Y].append((X, K))
    degree[X] += 1

for i in range(1, N+1):
    if degree[i] ==0:                       # 진입 차수가 0인것 = 기본 부품
        queue.append(i)

while queue:
    now = queue.popleft()                   # 현재 부품 꺼내기

    for next, cost in link[now]:            # 현재 부품과 연결된 (부품A.., 필요 개수) 꺼내기
        # 현 제품 : 기본 부품
        if needs[now].count(0) == N+1:      # index 0을 제외한 [0,0...0] 개수가 N개 = 기본부품
            needs[next][now] += cost         # 기본부품을 사용하는 next부품에 cost값 넣기 ex) [0, 0, 0, cost, 0..]

        # 현 제품 : 중간 부품
        else:
            for i in range(1, N + 1):       # now --(cost)--> next : 중간부품 now을 사용하는 부품 next
                needs[next][i] += needs[now][i] * cost
                                            # next 에 필요한 i 부품은? : now 부품에 필요한 i 부품 * 필요개수 를 누적
        degree[next] -= 1                   # i --(cost)--> now ---> next
        if degree[next] == 0:
            queue.append(next)              # 차수 0이면 큐에 넣음

for x in enumerate(needs[N]):               # enumerate : index 와 원소로 이루어진 튜플로 만들어 줌
    if x[1] > 0:
        print(*x)