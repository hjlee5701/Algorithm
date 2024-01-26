from collections import Counter
def solution(want, number, discount):
    myDict = {}
    for i in range(len(number)):
        myDict[want[i]] = number[i]
    maximum = sum(number)
    answer = 0
    for j in range(0, len(discount)-maximum+1):
        if myDict == dict(Counter(discount[j:j+maximum])):
            answer += 1
    return answer
print(solution(	["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
# print(solution(	["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))