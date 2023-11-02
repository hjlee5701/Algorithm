import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
def backtrack(idx):
    global totalNum, result
    if idx == N:
        totalNum = sum(abs(combLst[i] - combLst[i + 1]) for i in range(N-1))
        if totalNum > result:
            result = totalNum
        return
    for i in range(N):
        if visited[i]:
            continue
        combLst.append(A[i])
        visited[i] = True
        print("append, i -> ", combLst, i)
        backtrack(idx + 1)
        visited[i] = False
        combLst.pop()
        print("pop i-> ", combLst, i)
        

result = 0
combLst = []
visited = [False] * N

backtrack(0)

print(result)
