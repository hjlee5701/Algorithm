from sys import stdin
input = stdin.readline
N = int(input())
nLst = [int(input()) for _ in range(N)]

def merge_sort(nLst):
    if len(nLst) <=1:
        return nLst
    
    mid = len(nLst) // 2
    left = merge_sort(nLst[:mid])
    right = merge_sort(nLst[mid:])
    mer = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mer.append(left[i])
            i += 1
        else:
            mer.append(right[j])
            i += 1
    if i != len(left):
        mer += left[i:]
    if j != len(right):
        mer += right[j:]
    return mer

mer = merge_sort(nLst)