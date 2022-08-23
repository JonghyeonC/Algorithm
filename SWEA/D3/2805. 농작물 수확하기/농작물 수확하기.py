T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    total = 0
    for i in range(N//2+1):
        for j in range(N//2 - i, N//2 + 1 + i):
            total += arr[i][j]

    for i in range(N//2+1, N):
        for j in range(N//2 + i - (N-1), N//2 + N - i):
            total += arr[i][j]

    print(f'#{tc} {total}')