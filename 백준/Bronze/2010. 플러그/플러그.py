import sys
input = sys.stdin.readline

N = int(input())
plugs = []
for _ in range(N):
    plugs.append(int(input()))
print(sum(plugs) - (N - 1))