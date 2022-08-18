def dfs(v, f):
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w, f)
    if visited[f] == 1:
        return 1
    else:
        return 0


T = 10
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    V = 100
    adj_list = [[] for _ in range(V)]
    arr = list(map(int, input().split()))
    visited = [0] * V
    v, f = 0, 99
    for i in range(E):
        s, e = arr[i * 2], arr[i * 2 + 1]
        adj_list[s].append(e)

    print(f'#{tc} {dfs(v, f)}')