import sys
import heapq


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


V = int(input())
E = int(input())
adj = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
cnt = ans = 0
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))
prim(0, 1)
print(ans)