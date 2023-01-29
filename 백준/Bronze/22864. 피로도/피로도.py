a, b, c, m = map(int, input().split())

fatigue = 0
work = 0

if a > m:
    work = 0
else:
    for _ in range(1, 25):
        if fatigue <= m and a + fatigue <= m:
            fatigue += a
            work += b
        else:
            fatigue -= c
            if fatigue < 0:
                fatigue = 0
print(work)