t = int(input())
cnt = [0, 0, 0]

while t > 0:
    if t >= 300:
        t -= 300
        cnt[0] += 1
    elif t >= 60:
        t -= 60
        cnt[1] += 1
    elif t >= 10:
        cnt[2] += 1
        t -= 10
    else:
        break

if t != 0:
    print(-1)
else:
    print(*cnt)