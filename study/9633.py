def queen(row):
    global result
    if row == N:
        result += 1
        return

    for col in range(N):
        if (not pos[col] and not diagA[row+col] and not diagB[row-col + (N-1)]):
            pos[ col ] = diagA[ row+col ] = diagB[ row-col + (N-1)]  = True
            queen(row+1)
            pos[ col ] = diagA[ row+col ] = diagB[ row-col + (N-1) ] = False


from sys import stdin

N = int(stdin.readline())
result = 0
pos = [False] * N
diagA = [False] * (2*N-1)
diagB = [False] * (2*N-1)
queen(0)
print(result)

