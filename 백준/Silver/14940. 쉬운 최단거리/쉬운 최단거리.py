import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    visited[i][j] = 0
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] == -1:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = 0
for line in visited:
    print(*line)