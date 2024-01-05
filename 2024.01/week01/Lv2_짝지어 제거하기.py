def solution(s):
    stack = []

    for word in s:
        if stack and word == stack[-1]:
            stack.pop()
        else:
            stack.append(word)
    return 1 if len(stack) == 0 else 0


s = 'cdcd'
# s = 'baabaa'
print(solution(s))