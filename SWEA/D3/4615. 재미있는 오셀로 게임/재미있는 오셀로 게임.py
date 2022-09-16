T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2] = 2
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [-1, -1, 0, 1, 1, 1, 0, -1]
    for _ in range(M):
        x, y, c = map(int, input().split())
        i = x - 1
        j = y - 1
        point = []
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            while True:
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[nj][ni] == 0:
                    point = []
                    break
                elif arr[nj][ni] == c:
                    break
                elif arr[nj][ni] != c:
                    point.append((ni, nj))
                    nj += dj[k]
                    ni += di[k]
            if point:
                for x, y in point:
                    if c == 1:
                        arr[y][x] = 1
                    else:
                        arr[y][x] = 2
        arr[j][i] = c
    b = 0
    w = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                b += 1
            elif arr[i][j] == 2:
                w += 1
    print(f'#{tc} {b} {w}')