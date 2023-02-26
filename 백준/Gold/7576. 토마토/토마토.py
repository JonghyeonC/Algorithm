import sys
from collections import deque


def bfs(q):
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1
bfs(q)

ans = -2
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            visited[i][j] = -1

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and arr[i][j] != 1:
            ans = -1

if ans != -1:
    for i in range(N):
        for j in range(M):
            ans = max(ans, visited[i][j] - 1)
print(ans)