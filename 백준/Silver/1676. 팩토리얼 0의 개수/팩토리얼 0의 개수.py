def factorial(x):
    if x > 1:
        return x * factorial(x - 1)
    else:
        return 1


N = int(input())
result = str(factorial(N))[::-1]
ans = 0
flag = 0
for i in result:
    if flag == 1:
        break
    elif flag == 0:
        if i == "0":
            ans += 1
        else:
            flag = 1
print(ans)