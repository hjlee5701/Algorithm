import sys
from collections import deque
input=sys.stdin.readline

N, M =map(int,input().split())

bigLst=[[] for _ in range(N+1)]
smallLst=[[] for _ in range(N+1)]
mid=(N+1)/2

for i in range(M):
    a, b = map(int,input().split())

    bigLst[b].append(a)
    smallLst[a].append(b)

#bigger, smaller, list보고 n보다 크거나 작은 숫자 개수 파악
def dfs(arr, n):
    global cnt
    for i in arr[n]:
        if not visited[i]:
            visited[i]=True
            cnt+=1
            dfs(arr,i)

answer=0
for n in range(1,N+1):
    visited=[False]*(N+1)

    cnt=0
    dfs( bigLst, n )
    if cnt >= mid : answer += 1

    cnt=0
    dfs( smallLst,n )
    if cnt >= mid : answer += 1

print(answer)