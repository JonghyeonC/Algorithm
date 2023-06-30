N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = 0
for i in A:
    if i in B:
        ans += 1
print(N + M - 2 * ans)