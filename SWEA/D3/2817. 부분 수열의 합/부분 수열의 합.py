def f(n, r, s):
    global cnt
    if r == 0:
        if sum(p) == K:
            cnt += 1
    else:
        for i in range(s, n - r + 1):
            p[r-1] = arr[i]
            f(n, r-1, i+1)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for R in range(1, N+1):
        p = [0] * R
        f(N, R, 0)
    print(f'#{tc} {cnt}')