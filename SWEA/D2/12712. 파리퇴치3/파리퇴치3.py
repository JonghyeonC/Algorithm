T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]
    ans = 0
    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            if total > ans:
                ans = total
            total = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + dx[k] * l
                    nj = j + dy[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            if total > ans:
                ans = total

    print(f'#{tc} {ans}')