from sys import stdin
input = stdin.readline
N, K = map(int, input().split())
levels = [int(input()) for _ in range(N)]
levels.sort()

start, end = levels[0], levels[0]+K
res = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for lv in levels:
        if mid >= lv:
            total += mid - lv
    if total <= K:
        start = mid + 1
        res = mid
    else:
        end = mid - 1    

print(res)