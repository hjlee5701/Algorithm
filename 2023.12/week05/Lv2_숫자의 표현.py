def solution(n):
    answer = 0
    for i in range(1, n//2+1):
        total = i
        j = i+1
        while True:
            total += j
            if total == n:
                answer += 1
                break
            if total > n:
                break
            j+=1
    return answer+1

import sys
print(solution(int(input())))