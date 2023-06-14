X, Y = input().split()

X = X[::-1]
Y = Y[::-1]
result = int(X) + int(Y)
ans = str(result)[::-1]
print(int(ans))