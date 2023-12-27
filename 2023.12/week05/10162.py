import sys
T = int(sys.stdin.readline())

if T % 10 !=0:
    print(-1)
else:
    a = T//300
    T %= 300
    b = T//60
    T %= 60
    c = T//10
    T %= 10
    print(a, b, c)