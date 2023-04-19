import sys
import heapq


input = sys.stdin.readline
def prim(s, c):
    global cnt, ans
    # 그래프에서 하나의 꼭짓점을 선택하여 트리를 만든다.
    q = [(s, c)]
    # 모든 꼭짓점이 트리에 포함되어 있지 않은 동안
    while q:
        if cnt == V:
            break
        cost, target = heapq.heappop(q)
        if visited[target] == 0:
            visited[target] = 1
            ans += cost
            cnt += 1
            for next in adj[target]:
                # 트리와 연결된 변 가운데 트리 속의 두 꼭짓점을 연결하지 않는 가장 가중치가 작은 변을 트리에 추가한다.
                heapq.heappush(q, (next[0], next[1]))


V = int(input())
E = int(input())
adj = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)
cnt = ans = 0
# 그래프의 모든 변이 들어 있는 집합을 만든다.
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))
prim(0, 1)
print(ans)