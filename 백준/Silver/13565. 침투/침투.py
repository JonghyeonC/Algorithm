import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

for j in range(N):
    if arr[0][j] == 0:
        visited[0][j] = 1
        dfs(0, j)

flag = 0
for i in range(N):
    if visited[M - 1][i] == 1:
        flag = 1
if flag == 1:
    print('YES')
else:
    print('NO')