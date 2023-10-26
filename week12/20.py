# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         if s[0] == ")" or s[0] == "}" or s[0] == "]":
#             return False

#         for i in list(s.strip()):
#             if i == ")":
#                 if len(stack) == 0 : return False
#                 if stack[-1] == "(":
#                     stack.pop()
#                     continue
#             if i == "}":
#                 if len(stack) == 0 : return False
#                 if stack[-1] == "{":
#                     stack.pop()
#                     continue
#             if i == "]":
#                 if len(stack) == 0 : return False
#                 if stack[-1] == "[":
#                     stack.pop()
#                     continue
#             stack.append(i)
#
#         return True if len(stack) == 0 else False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        front = {'(':')', '[':']', '{':'}'}
        for element in s:
            if element in front:
                stack.append(element)
            else:
                if len(stack) == 0:
                    return False
                tmp = stack.pop(-1)
                if element != front[tmp]:
                    return False
        return True if len(stack) == 0 else False