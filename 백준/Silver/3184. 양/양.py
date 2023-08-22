from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    w = 0
    s = 0
    if arr[i][j] == 'v':
        w += 1
    elif arr[i][j] == 'o':
        s += 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                if visited[ni][nj] == 0:
                    if arr[ni][nj] == '.':
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                    elif arr[ni][nj] == 'v':
                        w += 1
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                    elif arr[ni][nj] == 'o':
                        s += 1
                        q.append((ni, nj))
                        visited[ni][nj] = 1
    if s > w:
        return 'sheep', s
    elif w >= s:
        return 'wolf', w
    elif s == 0 and w == 0:
        return 'x', 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
ans = [0, 0]
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0:
            if arr[i][j] == '.' or arr[i][j] == 'o' or arr[i][j] == 'v':
                name, cnt = bfs(i, j)
                if name == 'sheep':
                    ans[0] += cnt
                elif name == 'wolf':
                    ans[1] += cnt
print(*ans)