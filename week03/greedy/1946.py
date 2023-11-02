from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):

    N = int(input())
    applicant = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    cnt = 0
    low_rank = N

    for a, b in applicant:
        if b <= low_rank:
            low_rank = b
            cnt += 1
    print(cnt)