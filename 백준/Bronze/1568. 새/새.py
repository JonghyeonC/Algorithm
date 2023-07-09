N = int(input())
i = 1
ans = 0
while True:
    if N <= 0:
        break
    if i <= N:
        N -= i
        i += 1
    elif i > N:
        i = 1
        continue
    ans += 1
print(ans)