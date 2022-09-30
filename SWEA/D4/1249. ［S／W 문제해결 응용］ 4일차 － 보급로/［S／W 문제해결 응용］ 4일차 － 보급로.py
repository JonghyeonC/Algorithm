from collections import deque


def dijkstra(i, j):
    global cnt
    D[i][j] = 0
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if D[ni][nj] > D[i][j] + arr[ni][nj]:
                    D[ni][nj] = D[i][j] + arr[ni][nj]
                    q.append((ni, nj))


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    D = [[987654321] * N for _ in range(N)]
    cnt = 0
    i = 0
    j = 0
    dijkstra(i, j)
    print(f'#{tc} {D[N - 1][N - 1]}')