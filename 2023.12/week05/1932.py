# 1932_정수 삼각형
from sys import stdin
n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][j]=graph[i][j]+graph[i-1][j]

        elif j==len(graph[i])-1:
            graph[i][j]=graph[i][j]+graph[i-1][j-1]
        else:
            graph[i][j]=max(graph[i-1][j-1],graph[i-1][j])+graph[i][j]
            
print(max(graph[n-1]))


# 시간초과
# from sys import stdin
# n = int(stdin.readline())
# graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
# total = set()
# def triangle(k,length, res):
#     if length == n:
#         total.add(res)
#         return
#     res += graph[length][k]
#     triangle(k, length+1, res)
#     if k+1 < len(graph[length]):
#         graph[length][k+1]
#         triangle(k+1, length+1, res)

# triangle(0, 0, 0)
# print(max(total))