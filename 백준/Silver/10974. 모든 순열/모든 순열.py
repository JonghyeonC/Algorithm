def dfs(k):
    if k == r:
        print(*result)
    else:
        for i in range(N):
            if visited[i] == 0:
                result[k] = a[i]
                visited[i] = 1
                dfs(k + 1)
                visited[i] = 0


N = int(input())
a = [i for i in range(1, N + 1)]
r = N
result = [0] * r
visited = [0] * N
dfs(0)