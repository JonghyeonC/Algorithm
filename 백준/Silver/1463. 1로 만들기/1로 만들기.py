def f(n, cnt):
    global min_v
    if cnt > min_v:
        return
    if n == 1:
        min_v = min(min_v, cnt)
    else:
        if n % 3 == 0:
            f(n // 3, cnt + 1)
        if n % 2 == 0:
            f(n // 2, cnt + 1)
        f(n - 1, cnt + 1)


N = int(input())
min_v = 987654321
f(N, 0)
print(min_v)