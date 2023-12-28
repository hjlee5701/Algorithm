from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
lecture = list(map(int, input().split()))

start = max(lecture)            # 블루레이 크기 중 가장 작은 값
end = sum(lecture)              # 블루레이 크기 중 가장 큰 값
res = 0
while start <= end:
    mid = (start+end)//2        # 블루레이 크기 제한
    print('start,  mid, end, res ->', start, mid, end, res)
    cnt, total = 1, 0

    for time in lecture:
        if total + time > mid:  # 새로운 블루레이 추가
            cnt += 1
            total = 0
        total += time
    
    if cnt <= M:
        res = mid
        end = mid -1            # 최소값을 찾기 위해 범위 좁히기 
    else:
        start = mid + 1
print(res)