def bfs(i, j, num):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and arr[ni][nj] > num:
                    visited[ni][nj] = 1
                    q.append((ni, nj))


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_val = 0
ans = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] > max_val:
            max_val = arr[i][j]

for num in range(1, max_val):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > num and visited[i][j] == 0:
                cnt += 1
                bfs(i, j, num)
    if cnt > ans:
        ans = cnt
print(ans)
