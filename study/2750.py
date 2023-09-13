from sys import stdin
input = stdin.readline

N = int(input())
nLst = sorted(list(int(input()) for _ in range(N)), key=lambda x : x)
for n in nLst: print(n) 