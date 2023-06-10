import math, sys
input = sys.stdin.readline

N, M = map(int, input().split())
bun = 1001
per = 1001
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    bun = min(bun, a)
    per = min(per, b)

if bun > per * 6:   # 낱개가 무조건 더 저렴
    ans += N * per
elif bun < (N % 6) * per:   # 번들이 더 저렴
    ans += bun * math.ceil(N / 6)
else:   # 합쳐서 구매할 때
    ans += bun * (N // 6) + per * (N % 6)
print(ans)