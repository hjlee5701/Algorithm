from itertools import permutations

N = int(input())
num = list(range(1, N+1))
arr = list(permutations(num, N))
for i in arr:
    print(*i)