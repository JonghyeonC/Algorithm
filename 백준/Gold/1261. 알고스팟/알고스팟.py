from collections import deque
import sys


def bfs(i, j, cnt):
    q = deque()
    q.append((i, j, cnt))
    D[i][j] = cnt
    while q:
        i, j, cnt = q.popleft()
        if D[i][j] < cnt:
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    if D[ni][nj] > cnt:
                        D[ni][nj] = cnt
                        q.append((ni, nj, cnt))
                elif arr[ni][nj] == 1:
                    if D[ni][nj] > cnt + 1:
                        q.append((ni, nj, cnt + 1))
                        D[ni][nj] = cnt + 1
    return


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]
D = [[987654321] * N for _ in range(M)]
bfs(0, 0, 0)
print(D[M - 1][N - 1])