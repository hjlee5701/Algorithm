import sys
N = int(sys.stdin.readline())
top_list = list(map(int,sys.stdin.readline().split()))
stack = []

for idx, top in enumerate(top_list):
    while len(stack) != 0 and stack[-1][1] < top:
        stack.pop()
    
    if len(stack) == 0:
        print(0, end=" ")
    else:
        print(stack[-1][0] + 1, end=" ")    # index는 0 부터 시작해서 +1 처리
            
    stack.append((idx, top))