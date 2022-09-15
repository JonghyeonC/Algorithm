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
    return


N = int(input())
E = N + 1
c_1, c_2 = map(int, input().split())
M = int(input())
adjList = [[] for _ in range(E)]
for _ in range(M):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
visited = [0] * E
bfs(c_1)
if visited[c_2]:
    print(visited[c_2]-1)
else:
    print(-1)