N = int(input())
ans = 0
while N > 0:
    if N % 5 == 0:
        ans += N // 5
        N = 0
        break
    else:
        N -= 2
        ans += 1
if N == 0:
    print(ans)
else:
    print(-1)