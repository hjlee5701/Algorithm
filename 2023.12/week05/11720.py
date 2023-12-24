from sys import stdin
N = int(input())
print(sum(list(map(int, stdin.readline().strip()))))
# Enter로 개행문자(\n)가 발생함으로 strip()을 통해 공백-개행문자 제거를 해야 한다.