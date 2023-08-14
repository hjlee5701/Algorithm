def my_cards(combIdx):
    if combIdx == K:
        result.add("".join(combList))
        return

    for idx in range(0, N):
        if visited[idx]:
            continue

        visited[idx] = True
        combList[combIdx] = c_list[idx]
        my_cards(combIdx+1)
        visited[idx] = False

import sys
N = int(sys.stdin.readline())   
K = int(sys.stdin.readline())


visited = [False] * N
combList = [0] * K
c_list = []
for _ in range(N):
    c_list.append(input())

result = set()
my_cards(0)
print(len(result))