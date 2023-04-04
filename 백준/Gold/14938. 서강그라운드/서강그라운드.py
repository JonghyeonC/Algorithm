import sys


INF = 987654321
input = sys.stdin.readline
N, M, R = map(int, input().split())
arr = list(map(int, input().split()))
adj = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(R):
    s, e, w = map(int, input().split())
    adj[s][e] = w
    adj[e][s] = w

for t in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            if i == j:
                adj[i][j] = 0
            elif adj[i][j] > adj[i][t] + adj[t][j]:
                adj[i][j] = adj[i][t] + adj[t][j]

ans = 0
for i in range(1, N + 1):
    temp = 0
    for j in range(1, N + 1):
        if adj[i][j] <= M:
            temp += arr[j - 1]

    ans = max(ans, temp)

print(ans)
