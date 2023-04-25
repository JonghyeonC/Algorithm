from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        i, j, k = q.popleft()
        if i == N - 1 and j == M - 1:
            return visited[i][j][k]
        for x in range(4):
            ni = i + di[x]
            nj = j + dj[x]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj][k] == 0 and graph[ni][nj] == 0:
                    visited[ni][nj][k] = visited[i][j][k] + 1
                    q.append((ni, nj, k))
                elif visited[ni][nj][k] == 0 and graph[ni][nj] == 1 and k == 0:
                    visited[ni][nj][k + 1] = visited[i][j][k] + 1
                    q.append((ni, nj, k + 1))
    return -1


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

ans = bfs()
print(ans)