from sys import stdin

M = int(stdin.readline())
cards = set(map(int, stdin.readline().split()))

N = int(stdin.readline())
checks = list(map(int, stdin.readline().split()))

for i in checks:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")

# N = int(stdin.readline())
# cards = list(map(int, stdin.readline().split()))
# M = int(stdin.readline())
# checks = list(map(int, stdin.readline().split()))

# _dict = {}
# for i in range(len(cards)):
#     _dict[cards[i]] = 0
# print(_dict)

# for j in range(M):
#     if checks[j] not in _dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')