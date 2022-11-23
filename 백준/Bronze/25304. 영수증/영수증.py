total = int(input())
ans = 0
N = int(input())
for _ in range(N):
    money, a = map(int, input().split())
    ans += money * a
if total == ans:
    print('Yes')
else:
    print('No')