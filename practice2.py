import sys
N, M = map(int, sys.stdin.readline().split())
dLst = list((map(int, sys.stdin.readline().split())))
# dLst=sorted(dot_lst)
count = []*N
for j in range(M):
    # 선분의 시작과 끝
    left, right = map(int, sys.stdin.readline().split())

    # 점을 1개씩 꺼내움
    for i in range(N):
        while left <= right:

            mid = (left+right)//2
            if mid > dLst[i]:
                right = mid-1

            elif mid < dLst[i]:
                left = mid+1
                print('up->',left)
            else:
                count[i] = True
                break
    print(count)
print(count)

# lineLst = []
# for line in lineLst:
