def solution(n, words):
    stack = [words[0]]
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in stack:
            return [n, i//n+1] if (i+1)%n == 0 else [i%n+1, i//n+1]
        stack.append(words[i])
    return [0, 0]