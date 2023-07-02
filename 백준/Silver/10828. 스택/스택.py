import sys
input = sys.stdin.readline

N = int(input())
orders = []
for _ in range(N):
    order = input().split()
    if order[0] == "push":
        orders.append(int(order[1]))
    elif order[0] == "pop":
        if len(orders) != 0:
            print(orders.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(orders))
    elif order[0] == "empty":
        if len(orders) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "top":
        if len(orders) != 0:
            print(orders[-1])
        else:
            print(-1)