def f(n):
    global M
    q = []
    q.append(n)
    while q:
        n = q.pop(0)
        if n == M:
            return
        else:
            for nn in (n - 1, n + 1, 2 * n):
                if 0 <= nn < 100001 and dist[nn] == 0:
                    q.append(nn)
                    dist[nn] = dist[n] + 1


N, M = map(int, input().split())
dist = [0] * 100001
f(N)
print(dist[M])