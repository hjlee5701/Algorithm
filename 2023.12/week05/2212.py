import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))

if K >= N:
    print(0)
    sys.exit()

diff = sorted([sensor[i]-sensor[i-1] for i in range(1, N)])

for _ in range(K-1):
    diff.pop(0)

print(sum(diff))
    
