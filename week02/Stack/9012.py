import sys
T = int(sys.stdin.readline())
stack = []
for i in range(T):
    pList = list(sys.stdin.readline())
    sum = 0
    for ps in pList:
        if ps == '(':
            sum +=1
        elif ps == ')':
            sum -=1
        if sum < 0:
            print('NO')
            break
    if sum > 0: print('NO')
    elif sum == 0 :
        print("YES")