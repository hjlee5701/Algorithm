def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

print(solution(8, 4, 7)) # 3
print(solution(8, 4, 5)) # 3
print(solution(16, 5, 13)) # 4
print(solution(16, 15, 16)) # 1


# from math import ceil, log2
# def solution(n,a,b):
#     start, end = 1, n
#     if abs(a-b) == 1 and max(a,b) % 2 == 0:
#         return 1
#     while start < end:
#         mid = (start+end)//2
#         if a <= mid and b <= mid:
#             end = mid
#         elif mid < a and mid < b:
#             start = mid+1
#         else:
#             return int(ceil(log2(end-start)))      
