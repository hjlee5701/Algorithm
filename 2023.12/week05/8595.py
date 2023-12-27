import sys
n = int(sys.stdin.readline())
word = sys.stdin.readline().rstrip()

hiddenNum = ''
result = 0
for w in word:
    if w.isdigit():
        hiddenNum += w
    else:
        if len(hiddenNum) > 0:
            result += int(hiddenNum)
            hiddenNum = ''
  
if len(hiddenNum) > 0:
    result += int(hiddenNum)
        
print(result)

# 비효율
# import sys
# n = int(sys.stdin.readline())
# word = list(sys.stdin.readline().strip())

# numbers = [str(i) for i in range(10)]
# result, tmp = [], ''
# for i in range(n):
#     if word[i] in numbers:
#         tmp+=(word[i])
#         if i == n-1:
#             if len(tmp) > 6:
#                 tmp = tmp[0:6]
#             result.append(int(tmp))
#         continue    
#     if len(tmp) > 0:
#         if len(tmp) > 6:
#             tmp = tmp[0:6]
#         result.append(int(tmp))
#         tmp =''
    
# print(sum(result))