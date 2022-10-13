# dfs, 백트래킹
def dfs(i, j, cnt):
    global ans
    global flag
    if ans < cnt:
        ans = cnt
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] < arr[i][j] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1)
                visited[ni][nj] = 0
            elif arr[ni][nj] >= arr[i][j] and visited[ni][nj] == 0 and flag == 0:
                for minus in range(1, K + 1):
                    arr[ni][nj] -= minus
                    flag = 1
                    if arr[i][j] > arr[ni][nj]:
                        visited[ni][nj] = 1
                        dfs(ni, nj, cnt + 1)
                        visited[ni][nj] = 0
                    flag = 0
                    arr[ni][nj] += minus
            else:
                continue
        else:
            continue
    


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    flag = 0
    max_v = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_v:
                max_v = arr[i][j]
    max_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_v:
                max_list.append((i, j))
    for i, j in max_list:
        visited[i][j] = 1
        dfs(i, j, 1)
        visited[i][j] = 0
    print(f'#{tc} {ans}')