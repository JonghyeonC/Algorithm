T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
    i = j = 0
    for num in range(1, N ** 2 + 1):
        arr[i][j] = num

        i += di[k]
        j += dj[k]
        if not (0 <= i < N and 0 <= j < N and arr[i][j] == 0):
            i -= di[k]
            j -= dj[k]

            k = (k + 1) % 4
            i += di[k]
            j += dj[k]

    print(f'#{tc}')
    for temp in arr:
        print(' '.join(map(str, temp)))