from sys import stdin
input = stdin.readline
N, M = map(int, input().split())            # N: 사용날짜 M: 인출 횟수
days = [int(input()) for _ in range(N)]     # i 번째 날에 이용할 금액 (정렬X)

left, right = min(days), sum(days)          # 최소금액, 최대금액(total)
res = 0
print(days)
print("left, right : ", left, right)
while left <= right:
    mid = (left+right)//2
    print("mid : ", mid)
    money = mid                             # money : 한번에 인출 가능한 K원
    cnt = 1
    for i in range(N):
        if money < days[i]:                 # 인출한 K원보다 하루 동안 적은 돈을 사용
            cnt += 1                        # 인출 횟수
            money = mid                     # 다시 K원 인출
        money -= days[i]                    # K - 하루 사용한 돈

    # 인출 가능한 횟수 초과 or max+ 값 전까지 left를 +1 씩 이동
    if cnt > M or mid < max(days):
        left = mid + 1
    else:
        right = mid - 1
        res = mid                           # left(=mid) > right => result = mid
print(res)
    