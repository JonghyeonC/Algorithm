def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                cnt += 1
                visited[ni][nj] = 1
    return cnt


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i, j))
print(len(ans))
ans.sort()
for num in ans:
    print(num)