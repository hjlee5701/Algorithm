import sys
N, K = map(int, sys.stdin.readline().split())
numbers = list(sys.stdin.readline().strip())

stack = []
for num in numbers:
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))