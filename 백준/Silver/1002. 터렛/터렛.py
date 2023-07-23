import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    r_max = r1 + r2
    r_min = abs(r1 - r2)
    if d == 0 and r1 == r2:
        print(-1)
    elif d == r_max:
        print(1)
    elif d == r_min:
        print(1)
    elif d > r_max:
        print(0)
    elif d < r_min:
        print(0)
    else:
        print(2)
