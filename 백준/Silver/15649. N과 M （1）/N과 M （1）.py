from itertools import permutations


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
result = []
for temp in permutations(arr, M):
    result.append(temp)

for ans in result:
    print(*ans)