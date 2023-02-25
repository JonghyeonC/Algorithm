def dfs(x, visited):
    for node, dist in tree[x]:
        if visited[node] == 0:
            visited[node] = visited[x] + dist
            dfs(node, visited)


N = int(input())
tree = [[] for _ in range(N + 1)]
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)
for _ in range(N):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1, 2):
        tree[arr[0]].append((arr[i], arr[i + 1]))

dfs(1, visited_1)
visited_1[1] = 0

max_idx = visited_1.index(max(visited_1))
dfs(max_idx, visited_2)
visited_2[max_idx] = 0

print(max(visited_2))