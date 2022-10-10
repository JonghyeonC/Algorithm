N, M = map(int, input().split())
i, j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

visited[i][j] = 1
flag = 0
change = 0
while True:
    d -= 1
    if d == -1:
        d = 3
    ni = i + di[d]
    nj = j + dj[d]
    if arr[ni][nj] == 0 and visited[ni][nj] == 0:
        visited[ni][nj] = 1
        i = ni
        j = nj
        change = 0
        continue
    else:
        change += 1
    if change == 4:
        ni = i - di[d]
        nj = j - dj[d]
        if arr[ni][nj] == 0:
            i, j = ni, nj
        else:

            break
        change = 0

cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)