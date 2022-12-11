from collections import deque


def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((0, 0))
    visited[0][0] = 1
    temp = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= nj < M and 0 <= ni < N and visited[ni][nj] == 0:
                if arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                elif arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    temp += 1
                    visited[ni][nj] = 1
    return temp


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = []
time = 0
while True:
    cnt = bfs()
    time += 1
    if cnt != 0:
        ans.append(cnt)
    elif cnt == 0:
        break
print(time - 1)
print(ans[-1])