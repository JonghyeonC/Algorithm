def f(k, total):
    global ans
    if k == N:
        if total == S:
            ans += 1
    else:
        result[k] = 0
        f(k + 1, total)
        result[k] = 1
        f(k + 1, total + arr[k])


N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = [0] * N
ans = 0
f(0, 0)
if S == 0:
    ans -= 1
print(ans)