def findStr(idx):
    global result

    if idx == len(S):
        result = 1
        return
    
    if dp[idx]: return

    dp[idx] = 1

    for i in range(len(wordLst)):

        if len(S[idx:]) >= len(wordLst[i]):
            for w in range(len(wordLst[i])):
                if S[idx+w] != wordLst[i][w]:
                    break
            else:
                findStr(idx+ len(wordLst[i]))
    return

import sys
S = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())

dp = [0] * 101
sLen = len(S)
result = 0

wordLst = [sys.stdin.readline().strip() for _ in range(N)]
findStr(0)
print(result)