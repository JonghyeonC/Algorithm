A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    print((0 - A) * C + D + (B - 0) * E)
elif A == 0:
    print(D + (B - 0) * E)
elif A > 0:
    print((B - A) * E)