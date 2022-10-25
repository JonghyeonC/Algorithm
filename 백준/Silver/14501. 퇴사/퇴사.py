N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
money = [0] * (N + 1)
max_val = 0

for i in range(N-1, -1, -1):
    t = arr[i][0] + i

    if t <= N:
        money[i] = max(arr[i][1] + money[t], max_val)
        max_val = money[i]
    else:
        money[i] = max_val

print(max_val)
