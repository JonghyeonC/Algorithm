import sys
from collections import deque

def bfs(v):
    global cnt
    visited = [0] * N
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for w in adjlist[v]:
            if visited[w] == 0:
                cnt += 1
                q.append(w)
                visited[w] = 1


V, M = map(int, input().split())
N = V + 1
adjlist = [[] for _ in range(N)]
max_list = [0] * N
max_v = 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjlist[b].append(a)
for i in range(1, N):
    cnt = 1
    bfs(i)
    if cnt > max_v:
        max_v = cnt
    max_list[i] = cnt
for a, b in enumerate(max_list):
    if b == max_v:
        print(a, end=' ')



