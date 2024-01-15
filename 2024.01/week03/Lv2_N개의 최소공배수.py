# 유클리드 호제법
# https://adjh54.tistory.com/179
def solution(arr):
    result = 1
    for i in arr:
        result = lcm(result, i)
    return result

# 최대공약수
def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

# 최소공배수
def lcm(x, y):
    return x * y // gcd(x, y)

print(solution([2,6,8,14]))

# def solution(arr):
#     answer, k = max(arr), 0
#     while answer != k:
#         for num in arr:
#             if answer % num != 0:
#                 k+=1
#                 answer = max(arr) * k
#                 break
#         else:
#             return answer
#     return answer