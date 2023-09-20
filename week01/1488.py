import sys
input = sys.stdin.readline
N = int(input())

nums = list(map(int, input().split()))

add, sub, mul, div = map(int, sys.stdin.readline().split())

max_val, min_val = -sys.maxsize -1, sys.maxsize

def calculate(total, idx, add, sub, mul, div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        print('RETURN : idx-> ', idx)
        return 
    
    if add > 0:
        print('합 : idx , add -> ', idx, add)
        calculate(total + nums[idx], idx + 1, add - 1, sub, mul, div)
        print('합 복귀 : idx , add -> ', idx, add)
    if sub > 0:
        calculate(total - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        print('곱 : idx , mul -> ', idx, add)
        calculate(total * nums[idx], idx + 1, add, sub , mul -1, div)
        print('곱 복귀 : idx , mul -> ', idx, add)
    if div > 0:
        calculate(int(total / nums[idx]), idx + 1, add, sub, mul, div -1)


calculate(nums[0], 1, add, sub, mul, div)
print(max_val)
print(min_val)