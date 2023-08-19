import sys
N = int(sys.stdin.readline())
top_lst = list(map(int, sys.stdin.readline().split()))

# 최댓값 저장할 스택
stack = []

# 송신탑의 index를 저장
answer = []

for i in range(N):
    while stack:
        # 마지막에 저장된 탑 높이와 idx+1 번의 높이 값과 비교
        if stack[-1][1] > top_lst[i]:
            # 마지막에 배
            answer.append(stack[-1][0] + 1)
    if not stack: pass

    stack.append([i, top_lst[i]]) # 배열 인덱스, 값을 저장
print(answer)