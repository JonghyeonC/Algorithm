N, L = input().split()
N = int(N)
i = 0
ans = 0
while i != N:
    ans += 1
    if L in str(ans):
        continue
    i += 1
print(ans)