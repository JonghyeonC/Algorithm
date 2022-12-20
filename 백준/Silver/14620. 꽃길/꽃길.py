def dfs(cnt):
    global ans, total
    # flag = 0
    if cnt == 3:
        ans = min(ans, total)
        return
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            flag = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if visited[ni][nj] == 1:
                    flag = 1
            if flag == 0:
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 1
                    total += arr[ni][nj]
                dfs(cnt + 1)
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 0
                    total -= arr[ni][nj]


di = [0, 1, 0, -1, 0]
dj = [0, 0, 1, 0, -1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
total = 0
ans = 987654321
dfs(0)
print(ans)