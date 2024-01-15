# Lv2_카펫
def solution(brown, yellow):
    answer = [0, 0]
    S = brown + yellow
    for row in range(S-1, 0, -1):
        if S % row:  # 나눠 떨어질 때까지 반복문
            continue
        col = S // row
        yellow_S = (row - 2) * (col - 2)
        brown_S = S - yellow_S

        if yellow_S == yellow and brown_S == brown:
            answer[0], answer[1] = row, col
            break
        
    return answer