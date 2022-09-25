def tree(a, s, e):
    if a == K - 1:
        ans[a].append(arr[s])
        return
    else:
        c = (s + e) // 2
        ans[a].append(arr[c])
        tree(a + 1, s, c - 1)
        tree(a + 1, c + 1, e)


K = int(input())
arr = list(map(int, input().split()))
ans = [[] for _ in range(K)]
n = len(arr)
tree(0, 0, n)
for i in ans:
    for j in i:
        print(j, end=' ')
    print()