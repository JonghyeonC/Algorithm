def dfs(i, j, d, cnt):
    global answer
    ni = i + di[d]
    nj = j + dj[d]
    if ni == si and nj == sj:
        answer = max(answer, cnt)
        return
    if 0 <= ni < N and 0 <= nj < N:
        if visited[arr[ni][nj]] == 0:
            visited[arr[ni][nj]] = 1
            dfs(ni, nj, d, cnt + 1)
            if d < 3:
                dfs(ni, nj, d + 1, cnt + 1)
            visited[arr[ni][nj]] = 0


di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101
    answer = -1
    for i in range(N):
        for j in range(N):
            si = i
            sj = j
            visited[arr[i][j]] = 1
            dfs(i, j, 0, 1)
            visited[arr[i][j]] = 0
    print(f'#{tc} {answer}')