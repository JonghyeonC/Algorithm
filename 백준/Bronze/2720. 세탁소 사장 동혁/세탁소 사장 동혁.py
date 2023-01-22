coins = [25, 10, 5, 1]
N = int(input())
for _ in range(N):
    ans = [0] * 4
    change = int(input())
    for i in range(4):
        while change >= coins[i]:
            change -= coins[i]
            ans[i] += 1
    print(*ans)