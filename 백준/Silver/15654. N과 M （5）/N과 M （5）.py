from itertools import permutations


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
result = list(permutations(num_list, M))
for ans in result:
    print(*ans)