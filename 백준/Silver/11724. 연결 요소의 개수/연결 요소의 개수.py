import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v):
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
ans = 0

visited = [0] * N
for i in range(1, N):
    if visited[i] == 0:
        dfs(i)
        ans += 1
print(ans)