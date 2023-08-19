import sys
sys.setrecursionlimit(10**9)
pre = []
while True:                            
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break
def postorder(start, end):
    if start > end:
        return
    mid = end +1
    for i in range(start+1, end+1):
        if pre[start] < pre[i]:
            mid = i
            break
    postorder(start+1, mid-1)
    postorder(mid, end)
    print(pre[start])

postorder(0, len(pre)-1)