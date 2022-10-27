def dfs(v):
    print(v, end=' ')
    visited_d[v] = 1
    for w in adj[v]:
        if visited_d[w] == 0:
            dfs(w)


def bfs(v):
    q = []
    q.append(v)
    visited_b[v] = 1
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for w in adj[v]:
            if visited_b[w] == 0:
                q.append(w)
                visited_b[w] = 1


V, M, S = map(int, input().split())  # 정점의 개수, 간선의 개수, 시작 정점
N = V + 1
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    
for num_list in adj:
    num_list.sort()

visited_d = [0] * N
visited_b = [0] * N
dfs(S)
print()
bfs(S)