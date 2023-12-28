# x의 start, y의 start, x의 end, y의 end , 이전에 자른 방향(가로or세로)
def cutting(x_st, y_st, x_ed, y_ed, prevRowCut):
    
    dirty = []  # 불순물
    dia = 0     # 보석결정체
    
    for x in range(x_st, x_ed):
        for y in range(y_st, y_ed):
            if stones[x][y] == 1:
                dirty.append([x, y])
            elif stones[x][y] == 2:
                dia += 1
    
    if dia == 1 and len(dirty) == 0: return 1 # 제대로 석판 자름
    if dia == 0 or len(dirty) == 0 : return 0 # 잘못 자름

    count = 0   # 자르는 횟수

    if prevRowCut != True:
        for nx, ny in dirty:                # 불순물의 x,y 좌표
            can_cut = True                  # 자를 수 있는 여부
            for i in range(y_st, y_ed):
                if stones[nx][i] == 2:  # 불순물이 있는 nx줄(row)에 있는 y 중 다이아가 있는 경우 
                    can_cut = False
                    break                   # 다이아 있는 줄은 자를 수 없기 때문
            if can_cut:                     # nx줄에 있는 y 중 다이아가 없는 경우
                count += (cutting(x_st, y_st, nx, y_ed, True) * cutting(nx + 1, y_st, x_ed, y_ed, True)) 
                # x_ed를 nx로 업데이트해준다. x_st를 nx+1로 업데이트해준다.
                # x는 검토를 완료했으니, prevRowCut를 True로 바꾸어 밑의 if문(col줄)을 검사해준다.
                # 총 count = 왼쪽 석판에서 나온 count * 오른쪽 석판에서 나온 count

    if prevRowCut:
        for nx, ny in dirty:
            can_cut = True
            for i in range(x_st, x_ed):
                if stones[i][ny] == 2:  # 불순물이 있는 y줄(ny)에 있는 x 중 다이아가 있는 경우
                    can_cut = False
                    break
            if can_cut:                 # ny줄에 있는 x 중 다이아가 없는 경우
                count += (cutting(x_st, y_st, x_ed, ny, False) * cutting(x_st, ny + 1, x_ed, y_ed, False))
                # y_ed를 ny로 업데이트해준다. y_st를 ny+1로 업데이트해준다.

    return count

from sys import stdin
N = int(stdin.readline())

stones = [list(map(int, input().split())) for _ in range(N)]

result = cutting(0, 0, N, N, -1)
print(result if result != 0 else -1)