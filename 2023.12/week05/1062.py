import sys
from itertools import combinations
input=sys.stdin.readline

N,K=map(int,input().split())

alpha=['b','c','d','e','f','g','h','j','k','l','m','o','p','q','r','s',
    'u','v','w','x','y','z']

maximum=0
if K >= 5:
    possible=list(combinations(alpha,K-5))

    learned={'a','n','t','i','c'}
    words = [set(input().rstrip())-learned for _ in range(N)]

    for p in possible:
        cnt=0
        tmp = set(p)
        for word in words:
            if word.issubset(tmp):
                cnt+=1
        maximum=max(maximum,cnt)

    print(maximum)
else:
    print(maximum)