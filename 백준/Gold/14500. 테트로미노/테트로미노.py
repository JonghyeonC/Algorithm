import sys


def dfs(i, j, step, total):
    global ans

    if step == 4:
        ans = max(ans, total)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
            if step == 2:
                visited[ni][nj] = 1
                dfs(i, j, step + 1, total + arr[ni][nj])
                visited[ni][nj] = 0

            visited[ni][nj] = 1
            dfs(ni, nj, step + 1, total + arr[ni][nj])
            visited[ni][nj] = 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_val = max(map(max, arr))
visited = [[0] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0

print(ans)