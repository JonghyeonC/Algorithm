import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(v):
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)


V = int(input())
E = int(input())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N

if visited[1] == 0:
    dfs(1)

cnt = -1
for i in range(N):
    if visited[i] == 1:
        cnt += 1

print(cnt)