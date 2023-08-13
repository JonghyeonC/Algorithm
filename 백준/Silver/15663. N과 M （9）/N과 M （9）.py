from itertools import permutations


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = list(permutations(arr, M))
ans = set(ans)
ans = list(ans)
ans.sort()
for i in ans:
    print(*i)