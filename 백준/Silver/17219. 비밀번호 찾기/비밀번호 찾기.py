import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pwd = {}
for _ in range(N):
    a, b = input().split()
    pwd[a] = b
for _ in range(M):
    site = input().rstrip()
    print(pwd[site])