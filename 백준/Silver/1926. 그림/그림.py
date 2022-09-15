def bfs(i, j):
    global max_val
    q = []
    q.append((i, j))
    arr[i][j] += 1
    val = 0
    while q:
        i, j = q.pop(0)
        val += 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] += 1
    if max_val < val:
        max_val = val


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
max_val = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            bfs(i, j)

print(cnt)
print(max_val)