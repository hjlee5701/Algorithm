import sys
input = sys.stdin.readline

words = list(input().rstrip())
boom = input().rstrip()

stack = []
boom_len = len(boom)

for i in range(len(words)):
    stack.append(words[i])
    if ''.join(stack[-boom_len:]) == boom:
        for _ in range(boom_len):
            stack.pop()

print(res if (res:="".join(stack)) else "FRULA")