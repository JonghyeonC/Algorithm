def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in adjList[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1


V = int(input())
E = int(input())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
ans = 0

visited = [0] * N
bfs(1)
print(visited.count(2) + visited.count(3))