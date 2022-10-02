T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    dii = [1, 1, -1, -1]
    djj = [1, -1, -1, 1]
    ans = 0
    for i in range(N):
        for j in range(N):
            total_1 = arr[i][j]
            total_2 = arr[i][j]
            for k in range(4):
                for c in range(1, M):
                    ni = i + di[k] * c
                    nj = j + dj[k] * c
                    nii = i + dii[k] * c
                    njj = j + djj[k] * c
                    if 0 <= ni < N and 0 <= nj < N:
                        total_1 += arr[ni][nj]
                    if 0 <= nii < N and 0 <= njj < N:
                        total_2 += arr[nii][njj]
            if ans < max(total_1, total_2):
                ans = max(total_1, total_2)
    print(f'#{tc} {ans}')