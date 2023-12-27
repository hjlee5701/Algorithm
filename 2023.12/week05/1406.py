import sys
input = sys.stdin.readline

words = list(input().rstrip())
n = int(input())

stack = []
for i in range(n):
    command = input().split()

    if command[0] == "L" and words:
        stack.append(words.pop())
    elif command[0] == "D" and stack:
        words.append(stack.pop())
    elif command[0] == "B" and words:
        words.pop()
    elif command[0] == "P":
        words.append(command[1])
stack.reverse()
print("".join(words + stack))