def solution(n):
    count = bin(n).count('1')
    while True:
        n += 1
        tmp = bin(n).count('1')
        if count == tmp:
            return n
        
print(solution(78))