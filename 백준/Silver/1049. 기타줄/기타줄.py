import math

N, M = map(int, input().split())
bun = 1001
per = 1001
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    bun = min(bun, a)
    per = min(per, b)

if bun > per * 6:
    ans += N * per
elif bun < (N % 6) * per:
    ans += bun * math.ceil(N / 6)
else:
    ans += bun * (N // 6) + per * (N % 6)
print(ans)