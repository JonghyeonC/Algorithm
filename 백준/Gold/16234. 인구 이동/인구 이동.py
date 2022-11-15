def bfs(i, j):
    q = []
    q.append((i, j))
    union = []
    country = 0
    population = 0
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        union.append((i, j))
        country += 1
        population += arr[i][j]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if L <= abs(arr[i][j] - arr[ni][nj]) <= R:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
    while union:
        i, j = union.pop(0)
        arr[i][j] = population // country

    if country >= 2:
        return 1
    else:
        return 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    visited = [[0] * N for _ in range(N)]
    temp = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                temp += bfs(i, j)
    if temp:
        ans += 1
    else:
        break
print(ans)