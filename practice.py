import sys
N = int(sys.stdin.readline())

def backtrack(n):
    global x, y
    if N in result:
        print(len(list(result)))
        sys.exit()
    if n < 10:
        result.add(10*n + n)
        backtrack(10*n + n)
    else:
        x, y = n//10%10, n%10
        right = x + y
        val = 10*y + (right)%10
        result.add(val)
        backtrack(val)

count = 0
result = set()
x, y = 0, 0
backtrack(N)
