def is_valid(s):
    stack = []
    myDict = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in myDict.keys():  # (, {, [
            stack.append(char)
        else:  
            if not stack or char != myDict[stack.pop()]:
                return False
    return not stack  # 스택이 비어있으면 모든 괄호가 정상적으로 닫혔다는 의미

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:] + s[:i])
    return answer


print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}")) # 0
