def solution(s):
    value = 0
    answer = [0, 0]
    
    while value != 1:
        answer[1] += s.count("0")
        value = len(s) - s.count("0")
        s = format(value, 'b')
        answer[0] += 1
    
    return answer
