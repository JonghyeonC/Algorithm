coins = [500, 100, 50, 10, 5, 1]
money = 1000
cost = int(input())
change = money - cost
cnt = 0
for coin in coins:
    while change - coin >= 0:
        change -= coin
        cnt += 1

print(cnt)