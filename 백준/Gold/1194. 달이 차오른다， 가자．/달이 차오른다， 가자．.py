def bfs(x, y):
    q = []
    q.append((x, y, 0))
    visited[x][y][0] = 1
    while q:
        x, y, z = q.pop(0)
        if arr[x][y] == '1':
            print(visited[x][y][z] - 1)
            return
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != '#' and visited[nx][ny][z] == 0:
                    if arr[nx][ny].islower():
                        nz = z | (1 << (ord(arr[nx][ny]) - ord('a')))
                        if visited[nx][ny][nz] == 0:
                            visited[nx][ny][nz] = visited[x][y][z] + 1
                            q.append((nx, ny, nz))
                    elif arr[nx][ny].isupper():
                        if z & (1 << (ord(arr[nx][ny]) - ord('A'))):
                            visited[nx][ny][z] = visited[x][y][z] + 1
                            q.append((nx, ny, z))
                    else:
                        visited[nx][ny][z] = visited[x][y][z] + 1
                        q.append((nx, ny, z))
    print(-1)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            bfs(i, j)