hamburger = []
drinks = []
for _ in range(3):
    hamburger.append(int(input()))
for _ in range(2):
    drinks.append(int(input()))

ans = min(hamburger) + min(drinks) - 50
print(ans)