def dfs(r, k, s, total):
    global cnt
    if k == r:
        if total == S:
            cnt += 1
    else:
        for i in range(s, N - r + 1 + k):
            result[k] = arr[i]
            dfs(r, k + 1, i + 1, total + arr[i])


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    result = [0] * i
    dfs(i, 0, 0, 0)
print(cnt)