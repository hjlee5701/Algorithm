def solution(s):
    stack = []
    
    for tmp in s:
        if tmp == '(':
            stack.append(tmp)
        else:
            if len(stack) == 0 or stack[-1] == ')':
                return False
            stack.pop()
    return True if len(stack) == 0 else False
