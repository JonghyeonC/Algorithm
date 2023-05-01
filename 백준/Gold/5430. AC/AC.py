from collections import deque
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    orders = input().rstrip()
    N = int(input())
    tmp = list(input().rstrip()[1:-1].split(","))
    numbers = deque()
    for i in tmp:
        if i.isnumeric():
            numbers.append(i)
    cnt = 0
    flag = 0
    for order in orders:
        if order == "R":
            cnt += 1
        elif order == "D":
            if not numbers:
                print("error")
                flag = 1
                break
            if cnt % 2 == 1:
                numbers.pop()
            elif cnt % 2 == 0:
                numbers.popleft()
    if flag == 0:
        if cnt % 2 == 0:
            print("[" + ",".join(numbers) + "]")
        else:
            numbers.reverse()
            print("[" + ",".join(numbers) + "]")
