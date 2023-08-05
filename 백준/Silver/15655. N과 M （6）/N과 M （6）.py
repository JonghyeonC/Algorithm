from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = list(combinations(arr, M))
for i in ans:
    print(*i)