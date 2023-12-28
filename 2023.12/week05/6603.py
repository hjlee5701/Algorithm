from sys import stdin
from itertools import combinations
input = stdin.readline
while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    result = list(combinations(nums[1:], 6))
    for res in result:
        print(*res)
    print()

