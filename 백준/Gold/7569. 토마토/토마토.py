from collections import deque


def bfs(q):
    while q:
        z, i, j = q.popleft()
        for k in range(6):
            nz = z + dz[k]
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= nz < H and 0 <= ni < N and 0 <= nj < M and visited[nz][ni][nj] == 0 and arr[nz][ni][nj] == 0:
                arr[nz][ni][nj] = arr[z][i][j] + 1
                q.append((nz, ni, nj))


dz = [0, 0, 0, 0, -1, 1]
di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
q = deque()

day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1 and visited[h][n][m] == 0:
                q.append((h, n, m))
                visited[h][n][m] = 1

bfs(q)


for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 0:
                day = -1
max_value = -2
for h in range(H):
    for n in range(N):
        for m in range(M):
            max_value = max(arr[h][n][m], max_value)

if max_value != 1 and day != -1:
    print(max_value - 1)
elif day == -1:
    print(day)
elif max_value == 1:
    print(0)
