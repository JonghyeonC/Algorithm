T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    ans = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        dis_1 = (x1 - cx)**2 + (y1 - cy)**2
        dis_2 = (x2 - cx)**2 + (y2 - cy)**2
        r2 = r**2
        if dis_1 < r2 and dis_2 < r2:
            pass
        elif dis_1 < r2:
            ans += 1
        elif dis_2 < r2:
            ans += 1

    print(ans)