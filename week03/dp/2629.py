from sys import stdin
input = stdin.readline

# 추 : 개수 30개 이하 / 무게 최대 500g
W, weights = int(input()), list(map(int, input().split()))

# 구슬 : 개수 7개 이하 / 무게 최대 40000g
M, marvels = int(input()), list(map(int, input().split()))


dp = [[0 for _ in range((500 * idx)+1)] for idx in range(W+1)]


# 추로 판별할 수 있는 구슬의 무게를 나타내는 함수
def scale (idx, wgt):
    if idx > W :
        return
    if dp[idx][wgt] == 1: # 이미 같은 추의 무게와 개수로 방문했다면 return
        return
    dp[idx][wgt] = 1

    scale(idx+1, wgt + weights[idx-1]) # 추 넣기
    scale(idx+1, wgt)# 추 그대로 진행
    scale(idx+1, abs(wgt - weights[idx-1]))# 추 다른쪽에 넣기 (무게빼기)

scale(0, 0)

for marble in marvels:
    if marble > 500 * W:
        print('N', end=' ')
    elif dp[W][marble] == 1:
        print('Y', end=' ')
    else:
        print('N', end=' ')