import sys
n = int(sys.stdin.readline())
count = 0
def fibonacci(a, b):
    global count
    
    if count == n:
        print(a)
        return
    c = a  + b
    count +=1
    fibonacci(b, c)

fibonacci(0, 1)