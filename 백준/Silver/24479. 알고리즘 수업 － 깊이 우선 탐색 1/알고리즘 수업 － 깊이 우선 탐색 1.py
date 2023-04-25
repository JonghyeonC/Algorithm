import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start):
    global order
    visited[start] = order
    for adj in graph[start]:
        if visited[adj] == 0:
            order += 1
            dfs(adj)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
order = 1
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

dfs(R)

for ans in visited[1:]:
    print(ans)