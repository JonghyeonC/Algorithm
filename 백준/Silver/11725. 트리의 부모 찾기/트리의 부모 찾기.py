def bfs(n):
    q = []
    q.append(n)
    visited[n] = 1
    while q:
        n = q.pop(0)
        for i in tree[n]:
            if parents[i] == 0 and visited[i] == 0:
                parents[i] = n
                q.append(i)
                visited[i] = 1


N = int(input())
tree = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
bfs(1)

for i in range(2, N + 1):
    print(parents[i])