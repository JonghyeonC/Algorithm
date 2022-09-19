def dfs(x, y):
    global cnt
    visited[i][j] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
            if visited[nx][ny] == 0:
                cnt += 1
                dfs(nx, ny)
            else:
                cnt += visited[nx][ny]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_val = 0
    point = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt = 1
                dfs(i, j)
                visited[i][j] = cnt
                if cnt > max_val:
                    max_val = cnt
    for i in range(N):
        for j in range(N):
            if visited[i][j] == max_val:
                point.append(arr[i][j])
    ans = min(point)
    print(f'#{tc} {ans} {max_val}')