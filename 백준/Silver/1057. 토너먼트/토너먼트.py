N, a, b = map(int, input().split())
rud = 0
flag = 0
while a != b:
    if N < 2:
        flag = 1
        break
    else:
        if a % 2 == 0:
            a //= 2
        else:
            a = a // 2 + 1
        if b % 2 == 0:
            b //= 2
        else:
            b = b // 2 + 1
    rud += 1
    if N % 2 == 0:
        N //= 2
    else:
        N = N // 2 + 1
if flag == 1:
    print(-1)
else:
    print(rud)