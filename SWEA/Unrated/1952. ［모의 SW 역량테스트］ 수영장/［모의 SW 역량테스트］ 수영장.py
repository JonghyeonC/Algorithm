def f(mon, total):
    global min_val
    if total > min_val:
        return
    if mon >= 12:
        min_val = min(total, min_val)
    else:
        if arr[mon] == 0:
            f(mon + 1, total)
        else:
            # 1일권 이용
            f(mon + 1, total + arr[mon] * day)
            # 1달권 이용
            f(mon + 1, total + month)
            # 3달권 이용
            f(mon + 3, total + tri)


T = int(input())
for tc in range(1, T + 1):
    day, month, tri, year = map(int, input().split())
    arr = list(map(int, input().split()))
    min_val = year
    f(0, 0)
    print(f'#{tc} {min_val}')