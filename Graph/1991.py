import sys
N = int(sys.stdin.readline())
inputs = []
tree = {}
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

# 전위 : 루트 > left 재귀 > right 재귀 (위에서부터)
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 : left 재귀 > 루트 > right 재귀 (밑에서부터- 왼루오)
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위 : left 재귀 > right 재귀 > 루트 (왼All,오All, 루)
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()