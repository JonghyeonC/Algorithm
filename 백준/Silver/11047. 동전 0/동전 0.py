N, K = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)
coins.sort(reverse=True)
ans = 0
amount = K
for coin in coins:
    while amount >= coin:
        amount -= coin
        ans += 1
print(ans)