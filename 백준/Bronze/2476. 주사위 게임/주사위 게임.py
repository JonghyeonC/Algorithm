N = int(input())
res = 0
for i in range(N):
    num = input().split()
    num.sort()
    a, b, c = map(int, num)
    if a==b and b==c:
        money = 10000 + (a * 1000)
    elif a==b or a==c:
        money = 1000 + (b * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100
    if money > res :
        res = money
print(res)