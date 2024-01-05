def solution(n):
    prev, next, answer = 0, 0, 1
    for _ in range(n-1):
        prev, next = next, answer
        answer = (prev + next) % 1234567
    return answer
print(solution(48))