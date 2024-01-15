def solution(people, limit):
    answer, k = 0, 0
    people.sort()
    for i in range(len(people)-1, -1, -1):
        if k > i:
            break
        if people[i] + people[k] <= limit:
            k+=1
        answer+=1
        
    return answer