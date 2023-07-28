import sys
input = sys.stdin.readline


N = int(input().rstrip())
ans = set()
for _ in range(N):
    orders = input().rstrip().split()
    if len(orders) == 1:
        if orders[0] == "all":
            ans = set(i for i in range(1, 21))
        else:
            ans = set()
    else:
        order, num = orders[0], int(orders[1])
        if order == "add":
            ans.add(num)
        elif order == "remove":
            ans.discard(num)
        elif order == "check":
            print(1 if num in ans else 0)
        elif order == "toggle":
            if num in ans:
                ans.discard(num)
            else:
                ans.add(num)