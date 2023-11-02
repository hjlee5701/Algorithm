from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
thgs = list(map(int, input().split()))
multi = []

plugs = []
result = 0
for i in range(K):
    # 이미 있다면
    if thgs[i] in plugs:
        print('full -> ', plugs)
        continue

    # 빈공간이 있다면
    if len(plugs) != N:
        print('empty area -> ', plugs)
        plugs.append(thgs[i])
        continue

    # 가장 멀리 있는 플러그의 인덱스
    far_one = 0
    temp = 0

    # 현재 꽂혀있는 플러그들 확인
    for plug in plugs:
        # 앞으로 사용할 플러그에 없으면
        if plug not in thgs[i:]:
            temp = plug
            print('not in plug -> ', plug, thgs[i:])
            break
        # 현재까지 가장 멀리 있는 플러그보다 멀리 있으면
        elif thgs[i:].index(plug) > far_one:
            far_one = thgs[i:].index(plug)
            print('far far far -> ', far_one)
            temp = plug
    plugs[plugs.index(temp)] = thgs[i]
    # print('idx temp -> ', plugs[plugs.index(temp)])
    result += 1

print(result)
# 2 7
# 2 3 2 3 1 2 7