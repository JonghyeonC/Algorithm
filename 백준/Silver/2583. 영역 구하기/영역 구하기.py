def bfs(i,j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    return cnt


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = []
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and visited[i][j] == 0:
            ans.append(bfs(i, j))
ans.sort()
print(len(ans))
print(*ans)
