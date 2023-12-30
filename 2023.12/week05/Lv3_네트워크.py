def solution(n, computers):
    answer = 0
    connect = [False] * n

    def dfs(x):
        global answer
        if connect[x]:
            return
        
        connect[x] = True

        for i in range(n):
            if computers[x][i] and not connect[i]:
                dfs(i)

    for i in range(n):
        if not connect[i]:
            answer += 1
            dfs(i)

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# 3 [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))