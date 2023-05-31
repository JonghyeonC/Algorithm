N = int(input())
ans = 0
for i in range(N):
    tmp = sum(list(map(int, str(i))))
    if i + tmp == N:
       ans = i
       break
print(ans)