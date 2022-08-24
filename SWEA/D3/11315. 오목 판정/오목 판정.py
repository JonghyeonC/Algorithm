T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    di = [1, -1, 0, 1]
    dj = [1, 1, 1, 0]
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]
                    if cnt >= 5:
                        ans = 'YES'
    print(f'#{tc} {ans}')