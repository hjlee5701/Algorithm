from sys import stdin
input = stdin.readline

N = int(input())
cnt = int(input())

_dict = {i: [] for i in range(1, N+1)}

for i in range(cnt):
    a, b = map(int, input().split())
    _dict[a].append(b)
    _dict[b].append(a)

visited = [True] * 2 + [False] * N
result = 0

def dfs(k):
    global result
    for i in range(len(_dict[k])):
        if not visited[_dict[k][i]]:
            visited[_dict[k][i]] = True
            result += 1
            dfs(_dict[k][i])

dfs(1)
print(result)