import sys
input = sys.stdin.readline
from collections import deque


def bfs_map(i, j):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    arr[ni][nj] = cnt
                    visited[ni][nj] = 1


def bfs_find(v):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == v:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 0 and arr[ni][nj] != v:
                    return visited[i][j] - 1
                elif visited[ni][nj] == 0 and arr[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
    return 987654321


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = deque()
cnt = 1
ans = 987654321
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            arr[i][j] = cnt
            bfs_map(i, j)

for v in range(1, cnt + 1):
    ans = min(ans, bfs_find(v))

print(ans)
