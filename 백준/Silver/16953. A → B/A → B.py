a, b = map(int, input().split())

ans = 1

while b != a:
    temp = b
    if b % 10 == 1:
        b //= 10
        ans += 1
    elif b % 2 == 0:
        b //= 2
        ans += 1
    if temp == b:
        print(-1)
        break
else:
    print(ans)