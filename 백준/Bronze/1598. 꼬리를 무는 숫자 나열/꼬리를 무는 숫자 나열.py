A, B = map(int, input().split())
a = A % 4
aa = A // 4
b = B % 4
bb = B // 4
if a == 0:
    a = 4
if b == 0:
    b = 4
if A % 4 != 0:
    aa += 1
if B % 4 != 0:
    bb += 1
print(abs(a - b) + abs(aa - bb))