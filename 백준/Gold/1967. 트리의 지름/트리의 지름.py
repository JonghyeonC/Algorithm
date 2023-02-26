import sys
sys.setrecursionlimit(10 ** 9)


def dfs(x, visited):
    for node, dist in tree[x]:
        if visited[node] == 0:
            visited[node] = visited[x] + dist
            dfs(node, visited)


N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)
for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

visited_1[1] = 1
dfs(1, visited_1)

max_idx = visited_1.index(max(visited_1))

visited_2[max_idx] = 1
dfs(max_idx, visited_2)

print(max(visited_2) - 1)
