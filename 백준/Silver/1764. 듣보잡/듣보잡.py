import sys, heapq
input = sys.stdin.readline


N, M = map(int, input().split())
nosee = [input().rstrip() for _ in range(N)]
nohear = [input().rstrip() for _ in range(N)]
result = list(set(nosee) & set(nohear))
result.sort()
print(len(result))
for i in result:
    print(i)