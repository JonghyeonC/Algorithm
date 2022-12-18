from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[0] * L for _ in range(R)]
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < L and visited[ni][nj] == 0 and arr[ni][nj] == 'L':
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    temp = 0
    for x in range(R):
        for y in range(L):
            temp = max(temp, visited[x][y])
    return temp


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
R, L = map(int, input().split())
arr = [list(input()) for _ in range(R)]
cnt = 0
ans = 0
for i in range(R):
    for j in range(L):
        if arr[i][j] == 'L':
            cnt = bfs(i, j)
        ans = max(ans, cnt - 1)

print(ans)