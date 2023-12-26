from sys import stdin
N = int(stdin.readline())
result = 0
for i in range(1, N):
    tmp = i + sum(list(map(int, str(i))))
    if tmp == N:
        result = i
        break
print(result)