from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = 1


di = [1, 1, 0, -1, -1, -1, 0, 1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(h)]
        visited = [[0] * w for _ in range(h)]
        ans = 0
        for i in range(h):
            for j in range(w):
                if visited[i][j] == 0 and arr[i][j] == 1:
                    bfs(i, j)
                    ans += 1
        print(ans)