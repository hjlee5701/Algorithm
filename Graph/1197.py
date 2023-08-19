import sys
V, E = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])
parent = [i for i in range(V+1)]
answer = 0

def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_tree(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

for a, b, w in graph:
    if find_parent(a) != find_parent(b):
        union_tree(a, b)
        answer += w

print(answer)