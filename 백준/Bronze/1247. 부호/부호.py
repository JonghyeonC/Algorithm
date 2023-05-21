import sys
input = sys.stdin.readline


for _ in range(3):
    N = int(input())
    result = 0

    for _ in range(N):
        num = int(input())
        result += num

    if result > 0:
        print("+")
    elif result < 0:
        print("-")
    else:
        print("0")