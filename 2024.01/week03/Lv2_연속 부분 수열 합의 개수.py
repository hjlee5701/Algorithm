# Lv2_연속 부분 수열 합의 개수
def solution(elements):
    res = set()
    length = len(elements)

    for i in range(length):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+length):
            ssum += elements[j%length]
            res.add(ssum)
    return len(res)
    

    # 통과 시간 줄이기
    res = set(elements)
    length = len(elements)
    elements+=elements[:-1]

    for i in range(1, length+1):
        for j in range(length):
            res.add(sum(elements[j:j+i]))
    return len(res)

print(solution([7, 9, 1, 1, 4]))