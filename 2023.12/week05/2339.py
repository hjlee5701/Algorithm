# x의 start, y의 start, x의 end, y의 end , 이전에 자른 방향(가로or세로)
def cutting(x_st, y_st, x_ed, y_ed, prevRowCut):
    
    dirty = []  # 불순물
    dia = 0     # 보석
    
    for x in range(x_st, x_ed):
        for y in range(y_st, y_ed):
            if stones[x][y] == 1:
                dirty.append([x, y])
            elif stones[x][y] == 2:
                dia += 1
    
    if dia == 1 and len(dirty) == 0: return 1 # 제대로 석판 자름
    if dia == 0 or len(dirty) == 0 : return 0 # 잘못 자름

    count = 0   # 자르는 횟수

    if prevRowCut:							# 이전에 가로로 자름 -> 세로로 자르기
        for nx, ny in dirty:                # nx : 불순물의 x좌표
            can_cut = True                  # 자를 수 있는 여부
            for i in range(y_st, y_ed):
                if stones[nx][i] == 2:		# 불순물이 있는 nx줄에 y 중 보석 있음 -> 자르기 불가
                    can_cut = False
                    break
            if can_cut:                     # 불순물이 있는 nx줄에 있는 y 중 보석 없음
                count += (cutting(x_st, y_st, nx, y_ed, False) * cutting(nx + 1, y_st, x_ed, y_ed, False)) 
                # x줄의 end 지점을 nx로 변경 / x줄의 start 지점을 nx+1로 변경
                # 현재 세로로 석판을 잘랐음으로, prevRowCut 을 False 로 변경
                # count += 왼쪽 석판에서 나온 count * 오른쪽 석판에서 나온 count

    if prevRowCut != True:
        for nx, ny in dirty:                # ny : 불순물의 y좌표
            can_cut = True
            for i in range(x_st, x_ed):
                if stones[i][ny] == 2:  	# 불순물이 있는 ny줄에 x 중 보석 있음 -> 자르기 불가
                    can_cut = False
                    break
            if can_cut:                 	# 불순물이 있는 ny줄에 있는 x 중 보석 없음
                count += (cutting(x_st, y_st, x_ed, ny, True) * cutting(x_st, ny + 1, x_ed, y_ed, True))

    return count

from sys import stdin
N = int(stdin.readline())

stones = [list(map(int, input().split())) for _ in range(N)]

result = cutting(0, 0, N, N, -1)
print(result if result != 0 else -1)