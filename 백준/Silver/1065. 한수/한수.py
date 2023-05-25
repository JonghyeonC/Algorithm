N = int(input())
arr = [i for i in range(1, N + 1)]
ans = 0
flag = 0
for num in arr:
    tmp = list(str(num))
    if len(tmp) == 1:
        ans += 1
    else:
        diff = int(tmp[0]) - int(tmp[1])
        for i in range(0, len(tmp) - 1):
            if int(tmp[i]) - int(tmp[i + 1]) == diff:
                flag = 0
            else:
                flag = 1
                break
        if flag == 0:
            ans += 1
print(ans)
