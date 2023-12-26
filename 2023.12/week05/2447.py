# 2447_별 찍기 - 10
from sys import stdin
N = int(stdin.readline())

def draw_star(n):
    if n == 3:
        return ['***','* *','***']

    arr = draw_star(n//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(n//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(draw_star(N)))