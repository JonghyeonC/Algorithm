import sys
from collections import deque


def bfs(i, j, target):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == target and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1


def bfs_color(i, j, target):
    q = deque()
    q.append((i, j))
    visited_color[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if target == "R":
                if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] == "G" or arr[ni][nj] == "R") and visited_color[ni][nj] == 0:
                    q.append((ni, nj))
                    visited_color[ni][nj] = 1
            elif target == "G":
                if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] == "G" or arr[ni][nj] == "R") and visited_color[ni][nj] == 0:
                    q.append((ni, nj))
                    visited_color[ni][nj] = 1
            else:
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == target and visited_color[ni][nj] == 0:
                    q.append((ni, nj))
                    visited_color[ni][nj] = 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited_color = [[0] * N for _ in range(N)]

ans_normal = 0
ans_color = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "R" and visited[i][j] == 0:
            bfs(i, j, "R")
            ans_normal += 1
        elif arr[i][j] == "G" and visited[i][j] == 0:
            bfs(i, j, "G")
            ans_normal += 1
        elif arr[i][j] == "B" and visited[i][j] == 0:
            bfs(i, j, "B")
            ans_normal += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == "R" and visited_color[i][j] == 0:
            bfs_color(i, j, "R")
            ans_color += 1
        elif arr[i][j] == "G" and visited_color[i][j] == 0:
            bfs_color(i, j, "G")
            ans_color += 1
        elif arr[i][j] == "B" and visited_color[i][j] == 0:
            bfs_color(i, j, "B")
            ans_color += 1


print(f'{ans_normal} {ans_color}')