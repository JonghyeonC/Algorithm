import sys
input = sys.stdin.readline

for _ in range(3):
    list_y = list(map(int, input().split()))
    result = list_y.count(0)
    if result == 1: 
        print("A")
    elif result == 2:
        print("B")
    elif result == 3:
        print("C")
    elif result == 4:
        print("D")
    else:
        print("E")