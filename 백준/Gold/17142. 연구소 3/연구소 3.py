from itertools import combinations
from collections import deque


def bfs(q):
    visited = [[-1] * N for _ in range(N)]
    for x, y in q:
        visited[x][y] = 0
    while q:
        i, j = q.popleft()
        if visited[i][j] == -1:
            visited[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == -1:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    max_v = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                continue
            if visited[i][j] == -1:
                return 987654321
            else:
                max_v = max(max_v, visited[i][j])
    return max_v


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 987654321
virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))

com_viruses = list(combinations(virus, M))

for virus_list in com_viruses:
    q = deque()
    for viruses in virus_list:
        q.append(viruses)
    ans = min(ans, bfs(q))
print(ans if ans != 987654321 else -1)