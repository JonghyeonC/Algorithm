import copy


def virus():
    global ans
    n_arr = copy.deepcopy(arr)
    q = []
    for i in range(N):
        for j in range(M):
            if n_arr[i][j] == 2:
                q.append((i, j))
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and n_arr[ni][nj] == 0:
                n_arr[ni][nj] = 2
                q.append((ni, nj))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if n_arr[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)


def wall(k):
    if k == 3:
        virus()
        return
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    wall(k + 1)
                    arr[i][j] = 0


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
wall(0)
print(ans)