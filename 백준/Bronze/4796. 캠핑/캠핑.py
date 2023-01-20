case = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        case += 1
        cnt = 0
        while V >= P:
           V -= P
           cnt += 1
        if V >= L:
            print(f'Case {case}: {cnt * L + L}')
        elif V < L:
            print(f'Case {case}: {cnt * L + V}')
