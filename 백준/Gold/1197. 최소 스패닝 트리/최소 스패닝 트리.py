import heapq
import sys
input = sys.stdin.readline


def prim(s, c):
    global cnt, ans
    q = [(s, c)]
    while q:
        if cnt == V:
            break
        cost, target = heapq.heappop(q)
        if visited[target] == 0:
            visited[target] = 1
            ans += cost
            cnt += 1
            for next in adj[target]:
                heapq.heappush(q, (next[0], next[1]))


V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
ans = 0
cnt = 0
for _ in range(E):
    c, p, w = map(int, input().split())
    adj[c].append((w, p))
    adj[p].append((w, c))
prim(0, 1)
print(ans)
# https://blog.naver.com/dhkimxx/222745059230