# -큰수 + 작은수
from sys import stdin
input = stdin.readline


#'-'를 기준으로 split
sepArr = input().split('-')

#'+' 연산의 합들을 저장할 리스트
sumNum = []

for i in sepArr:
    plus = 0

    #'-'를 기준으로 split
    tmp = i.split('+')

    for j in tmp:
        plus += int(j)

    sumNum.append(plus)

#식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다
n = sumNum[0]

for i in range(1,len(sumNum)): #1번째 값부터 n에서 빼준다
    n -= sumNum[i]
print(n)