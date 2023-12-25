X = input()

# 16진수인 경우
if X[:2] == '0x':
    print(int(X, 16))
# 8진수인 경우
elif X[0] == '0':
    print(int(X, 8))
else:
    print(int(X))