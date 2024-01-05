from collections import deque
def check_one_word(word,begin):
    counting = 0
    for w,b in zip(word,begin):
        if w != b:
            counting +=1
    return True if counting ==1 else False

def solution(begin,target,words):
    if target not in words:
        return 0
    queue = deque()
    queue.append([begin,[]])
    
    while queue:
        begin, visited = queue.popleft()
        print("--------------- start ---------------", )
        print("begin, visited : ", begin, visited)
    
        
        for word in words:
            if word not in visited and check_one_word(word,begin):
                if word == target:
                    return len(visited)+1
                else:
                    temp = (visited[:])
                    temp.append(word)
                    queue.append([word,temp])
            print(queue)
        print()

begin = "hit"
target = "cog"
words = ["cog","hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))