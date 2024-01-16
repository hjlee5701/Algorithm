from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter_dict = Counter(tangerine)
    for cnt in sorted(counter_dict.values(), reverse=True):
        answer += 1
        k -= cnt
        if k <= 0:
            return answer
    return answer

# 통과 시간 줄이기
# from collections import Counter
# def solution(k, tangerine):
#     counter_dict = Counter(tangerine)
#     sorted_tuples = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
#     arr = [item[0] for item in sorted_tuples]

#     cnt, kinds = 0, 0
#     for a in arr:
#         cnt += counter_dict[a]
#         kinds += 1
#         if cnt >= k:
#             return kinds
#     return kinds


# print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
# print(solution(2, [1, 2, 9, 3, 4, 5, 6, 7, 9, 9])) # 1
# print(solution(3, [1, 1, 2, 2])) # 2
# print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
# print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1