arr = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[j][i] += 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[j][i] > 0:
            cnt += 1
print(cnt)