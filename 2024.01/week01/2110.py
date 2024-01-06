from sys import stdin
input = stdin.readline
N, C = map(int, input().split())         # N : 집 수, C : 공유기 수
home = [int(input()) for _ in range(N)]  # 집 좌표

home.sort()
start, end = 0, home[-1]-home[0]        # 집 사이 최소/최대 거리
res = 0

while start <= end:
    mid = (start + end)//2          # 최소/최대 거리 중앙값
    cnt = 1
    last = home[0]                  # 마지막으로 설치된 공유기의 위치

    for i in range(N):
        if home[i] - last >= mid:
            cnt+=1
            last = home[i]

    if cnt >= C:                    # 공유기 C개 이상 설치
        start = mid + 1
        res = mid
    else:                           # 공유기 C개 미만 설치됨
        end = mid - 1
print(res)