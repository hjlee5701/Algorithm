import sys
N = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(N)]

tallest = stack[-1]
result = 1
for i in range(len(stack)-1, -1, -1):
    if stack[i] > tallest:
        result +=1
        tallest = stack[i]
print(result)