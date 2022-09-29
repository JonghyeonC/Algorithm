def prim(s):
    D[s] = 0
    for _ in range(N):
        u = 0
        min_v = float("inf")
        for v in range(N):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v
        visited[u] = 1
        for v in range(N):
            if not visited[v]:
                if D[v] > adj[u][v]:
                    D[v] = adj[u][v]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    D = [float("inf")] * N
    visited = [0] * N
    adj = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            adj[i][j] = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) * E
            adj[j][i] = adj[i][j]
    prim(0)
    print(f'#{tc} {round(sum(D))}')