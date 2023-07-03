import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
orders = deque()
for _ in range(N):
    order = input().split()
    if order[0] == "push":
        orders.append(int(order[1]))
    elif order[0] == "pop":
        if len(orders) != 0:
            print(orders.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(orders))
    elif order[0] == "empty":
        if len(orders) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(orders) != 0:
            print(orders[0])
        else:
            print(-1)
    elif order[0] == "back":
        if len(orders) != 0:
            print(orders[-1])
        else:
            print(-1)