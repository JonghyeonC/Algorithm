from itertools import combinations_with_replacement


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = list(combinations_with_replacement(arr, M))
for ans in result:
    print(*ans)