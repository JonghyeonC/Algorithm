def f(n):
    global cnt
    if n > N:
        return
    if n == N:
        cnt += 1
    else:
        for x in [n + 1, n + 2, n + 3]:
            f(x)


T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    f(0)
    print(cnt)