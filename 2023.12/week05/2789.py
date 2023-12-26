from sys import stdin
N, M = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))

result = set([])
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = cards[i]+cards[j]+cards[k]
            if tmp <= M:
                result.add(tmp)

print(max(result))