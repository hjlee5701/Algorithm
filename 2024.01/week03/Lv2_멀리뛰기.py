# 피보나치수열
def solution(n):
    if n<3:
        return n
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
        print(dp)
    return dp[n]%1234567

# 시간초과
# from itertools import product
# def solution(n):
#     arr = [1, 2]
#     res = 0
#     for i in range(1, n+1):
#         for nums in product(arr, repeat=i):
#             if sum(nums) == n:
#                 res += 1
#     return res%1234567

print("n=3 : ", solution(3))
print()
print("n=4 : ", solution(4))
print()
print("n=5 : ", solution(5))
print()