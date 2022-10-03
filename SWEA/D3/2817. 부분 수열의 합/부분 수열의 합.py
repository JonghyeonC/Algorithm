def f(k, total):
    global cnt
    if k == N:
        if total == K:
            cnt += 1
    else:
        f(k + 1, total)
        f(k + 1, total + arr[k])


T = int(input())
for tc in range(1, T  +  1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    f(0, 0)
    print(f'#{tc} {cnt}')