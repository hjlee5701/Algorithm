import sys
N = int(sys.stdin.readline())

words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())

wordLst = sorted( words, key=lambda x : (len(x), x))
print(wordLst)
word_set = set()
print('시작')
for i in word_set: print(i)
