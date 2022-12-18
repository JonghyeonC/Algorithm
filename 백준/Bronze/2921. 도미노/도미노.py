N = int(input())
ans = 0
for num in range(1, N + 1):
    for i in range(num, num + num + 1):
        ans += i
print(ans)