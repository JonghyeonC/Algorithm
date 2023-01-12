A, B, C = map(int, input().split())
time = [0] * 101
for _ in range(3):
    a, b = map(int, input().split())
    for i in range(a, b):
        time[i] += 1
ans = 0
for num in time:
    if num == 1:
        ans += num * A
    elif num == 2:
        ans += num * B
    elif num == 3:
        ans += num * C
print(ans)
